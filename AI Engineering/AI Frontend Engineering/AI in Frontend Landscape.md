# AI in Frontend Landscape


### 1. Vercel AI SDK & Integration Layer

**Category:** FRAMEWORK / LIBRARY CONCEPT
**Section:** LLM Application Techniques

| **Concept** | **Core Mental Model** | **Version/API Surface** | **When to Reach For It vs Alternatives** | **Gotchas & Breaking Changes** | **Resources** |
| --- | --- | --- | --- | --- | --- |
| **Vercel AI SDK** | The synchronization engine between backend agent loops (tool execution, LLM network calls) and frontend React state. It splits reality into `ModelMessage` (what the LLM sees) and `UIMessage` (what React renders). | **v5+**: `streamText`, `tool`, `convertToModelMessages`, `useChat`. Heavily relies on Zod for schema definitions. | **Use for:** 95% of Next.js AI features involving streaming or tool calling. **Alternatives:** LangChain.js (heavyweight, steep learning curve), direct provider SDKs (painful manual SSE parsing). | Treating it just as a text streamer. Its actual value is managing recursive tool-calling loops (`stepCountIs`) without you writing the recursion manually. | Vercel AI SDK Docs |

**What's Missing:**

- You didn't mention how to handle **custom provider abstraction**. If you swap OpenAI for Anthropic, you need to know how the SDK handles differing system prompt injection or token-limit behaviors under the hood.
- No mention of `streamObject` vs `streamText` limitations — specifically how `streamObject` handles malformed JSON chunks during connection drops.

### 2. AI-Specific Prebuilt UI Layers

**Category:** FRAMEWORK / LIBRARY CONCEPT
**Section:** Low-Level Design — UI Patterns

| **Concept** | **Core Mental Model** | **Version/API Surface** | **When to Reach For It vs Alternatives** | **Gotchas & Breaking Changes** | **Resources** |
| --- | --- | --- | --- | --- | --- |
| **AI UI Components** | UI libraries built specifically for the asynchronous, non-deterministic nature of AI (typing effects, markdown streaming, stop buttons) so you don't rebuild them for the 10th time. | `assistant-ui` hooks, Vercel AI Elements (Shadcn registry style), CopilotKit (`useCopilotReadable`). | **Use for:** Dedicated chatbots or copilots. **Alternatives:** Standard UI libs like MUI/Ant (lacks AI lifecycle hooks, terrible DX for streaming), building from scratch (massive time sink). | Trying to force standard React state to manage "generating" vs "thinking" vs "done" phases. Use the library's built-in state machines. | assistant-ui docs, Vercel AI Elements |

**What's Missing:**

- **Markdown parsing performance.** Most of these use `react-markdown`. If an LLM streams a 4000-token code block, re-rendering the entire markdown AST on every chunk will absolutely tank browser FPS. You need memoization strategies for the parsed AST.

### 3. Partial JSON Streaming & AI UI State

**Category:** UI/SYSTEM DESIGN PATTERN
**Section:** Low-Level Design — UI Patterns

| **Pattern** | **Problem It Solves** | **Key Implementation Details** | **Edge Cases & Failure Modes** | **Real-world Examples** |
| --- | --- | --- | --- | --- |
| **Partial JSON Streaming** | LLM latency for structured data is too high. Users won't wait 8 seconds for a JSON object to fully resolve before seeing UI updates. | Use `useObject` alongside a Zod schema. The hook returns a deeply partial, optimistically populated object. Map over the array/object keys as they stream in over the wire. | **Edge Case:** Accessing deeply nested properties that haven't streamed yet causes `undefined` crashes. Optional chaining (`?.`) is mandatory everywhere. | Live report generation, dynamic form auto-filling, real-time dashboard building. |

**What's Missing:**

- **Connection interruptions.** If the stream drops halfway through a JSON array, you need a strategy to either discard the broken tail end or prompt the LLM to resume from the last valid token.

### 4. Client-Side Tool Rendering (Generative UI)

**Category:** UI/SYSTEM DESIGN PATTERN
**Section:** Low-Level Design — UI Patterns

| **Pattern** | **Problem It Solves** | **Key Implementation Details** | **Edge Cases & Failure Modes** | **Real-world Examples** |
| --- | --- | --- | --- | --- |
| **Client-Side Tool Mapping** | Users want to take actions, not just read text. Generative UI shifts the output from markdown to functional components. | Server yields a JSON tool call (`{ toolName: 'sign_txn', args: {...} }`). Client intercepts the `toolInvocation` array and maps it to a React component instead of rendering text. | **Failure Mode:** LLM hallucinates a prop your component doesn't expect, or omits a required one, breaking the React render tree. Validate args before rendering. | Financial dashboards (rendering a chart instead of text), e-commerce (rendering a checkout button). |

**What's Missing:**

- **State hydration during SSR.** If a user refreshes a page with a completed tool call in their history, you need to know how to hydrate that historical JSON back into the interactive React component without re-triggering the LLM.

### 5. LLM Caching Strategies

**Category:** APPLIED TECHNIQUE / STRATEGY
**Section:** LLM Application Techniques

| **Technique** | **What It Actually Means** | **Why It Matters** | **How It's Applied in Practice** | **Common Misconceptions / Gotchas** |
| --- | --- | --- | --- | --- |
| **Semantic Caching** | Intercepting LLM requests based on the *meaning* of the prompt (via embeddings) rather than an exact string match. | LLMs are slow and expensive. Bypassing them for frequent, similar queries ("reset password" vs "forgot password") drastically cuts costs and latency. | Usually handled via a dedicated AI Gateway (Portkey, Helicone) sitting between your Next.js API and OpenAI, or via Redis/Upstash for exact-match caching. | **Gotcha:** You can't easily cache and re-stream an SSE connection natively in Next.js App Router. Cache hits usually return static text instantly, requiring your frontend to handle both stream and static response types. |

**What's Missing:**

- **Cache Invalidation.** Semantic caching is dangerous if the underlying ground-truth data changes (e.g., a product price updates, but the semantic cache still returns the old price). You need cache-busting tied to your database webhooks.

### 6. Multimodal Voice Input

**Category:** PROTOCOL / API PARADIGM / COMMUNICATION PATTERN
**Section:** Networking — API Paradigms

| **Topic** | **Core Concepts & Mental Model** | **Tools & Libraries** | **Key Techniques** | **Tradeoffs & Failure Modes** | **Resources** |
| --- | --- | --- | --- | --- | --- |
| **WebRTC for LLM Voice** | Real-time conversational AI requires sub-second latency and the ability for the user to interrupt the model mid-sentence. Standard HTTP cannot do this. | LiveKit, Daily, OpenAI Realtime API. | Connecting frontend React components directly to the model via WebRTC for bidirectional audio streaming and echo cancellation. | **Tradeoffs:** High infrastructure complexity. **Failure Mode:** Trying to pipe audio chunks over standard WebSockets/SSE results in terrible lag and overlapping audio. | LiveKit Docs |

**What's Missing:**

- **Mobile Browser Permissions.** Managing the `getUserMedia` microphone permissions lifecycle in Safari iOS, which is notoriously aggressive about killing background audio tracks.

### 7. AI Frontend Security (Tool Validation & HITL)

**Category:** SECURITY / BROWSER MECHANISM
**Section:** Security

| **Topic** | **Core Concepts & Mental Model** | **Tools & Libraries** | **Key Techniques** | **Tradeoffs & Failure Modes** | **Resources** |
| --- | --- | --- | --- | --- | --- |
| **Frontend Payload Validation** | The UI must treat LLM tool-call outputs as untrusted user input. You cannot blindly execute actions based on AI instructions. | Zod, `@upstash/ratelimit`. | **1. Zod Parsing:** Validate all incoming tool args. **2. HITL (Human in the loop):** Pause execution and render a `<ConfirmDialog>` for any destructive action. | **Failure Mode:** Putting API keys or unprotected rate-limiting logic on the client. Always proxy through a Next.js API route. | OWASP for LLMs |

**What's Missing:**

- **Prompt Injection via UI state.** If an LLM reads user-generated content from the page (e.g., summarizing a PDF the user uploaded), that PDF might contain invisible text instructing the LLM to execute a malicious tool call.

### 8. UI-Layer LLM Observability

**Category:** APPLIED TECHNIQUE / STRATEGY
**Section:** LLM Application Techniques

| **Technique** | **What It Actually Means** | **Why It Matters** | **How It's Applied in Practice** | **Common Misconceptions / Gotchas** |
| --- | --- | --- | --- | --- |
| **Frontend Trace Injection** | Passing trace IDs from the client browser all the way through the server and into the LLM provider to track the full lifecycle of a generation. | When a user complains about a weird AI response, you need to map their specific button click to the exact prompt, tool results, and latency of that generation. | Inject trace IDs into headers. Use `experimental_telemetry` in AI SDK. Pipe data to Braintrust or Langfuse. | **Misconception:** OpenAI/Anthropic dashboards are enough. They only show raw API usage; they cannot tell you which React component triggered the cost spike. |

**What's Missing:**

- **PII Scrubbing.** Observability tools will log full prompts and responses by default. You need middleware to scrub passwords, session tokens, or sensitive user data *before* it hits Langfuse/Braintrust.