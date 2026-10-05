# Agentic AI Interview Questions

---

## Autonomous Agent Fundamentals & Architectures
1. What defines an "AI Agent" compared to a simple LLM prompt-completion call?
2. Explain the ReAct (Reason + Act) design pattern. How does the agent loop between thought, action, and observation?
3. What is the difference between Plan-and-Solve (Reflection/Reflexion) and step-by-step Reactive agent architectures?
4. How do agents maintain Memory (Short-Term working memory in context window vs Long-Term episodic/semantic memory in Vector DBs)?
5. How do you prevent infinite execution loops and enforce budget/token caps in autonomous agent loops?

---

## Function Calling & Tool Use
1. How does Function Calling / Tool Calling work under the hood between the LLM and the runtime environment?
2. How do you provide JSON Schemas for tools, and what happens when an LLM hallucinate invalid parameters or types?
3. How do you implement Parallel Tool Calling, and how do you handle partial failures when executing multiple tools?
4. How do you design "Human-in-the-Loop" approvals for high-stakes or destructive tool actions (e.g. database deletes, payments, emails)?

---

## Model Context Protocol (MCP)
1. What is the Model Context Protocol (MCP), and what architectural problem does it solve in LLM tool integration?
2. What is the difference between an MCP Client, an MCP Host, and an MCP Server?
3. What are the core primitives exposed by MCP servers: Resources, Tools, and Prompts?
4. What transports are supported by MCP (stdio vs Server-Sent Events / SSE), and what are the security considerations?
5. How does MCP standardize context sharing across multiple development environments and IDEs?

---

## Orchestration Frameworks (LangGraph, CrewAI, AutoGen)
1. What are the limitations of linear DAG (Directed Acyclic Graph) pipelines like standard LangChain chains when building real-world agents?
2. How does LangGraph model cyclical workflows, conditional routing, state persistence (checkpointing), and time-travel debugging?
3. What is the difference between Hierarchical Multi-Agent orchestration (Supervisor/Worker pattern) vs Collaborative Multi-Agent conversation (AutoGen/CrewAI)?
4. How do you coordinate sub-agents with specialized system prompts and restricted tool access?
5. How do you write unit and integration tests for non-deterministic multi-agent workflows?
