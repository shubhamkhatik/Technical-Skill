# AI System Design Interview Questions

---

## Architecture Principles for Enterprise AI Systems
1. What are the core trade-offs between Latency, Cost, Context Size, and Output Quality in production GenAI systems?
2. How do you implement Semantic Caching (GPTCache) to return cached responses for semantically similar user prompts and save 40-70% on token costs?
3. How do you design an LLM Router / Cascading Gateway (routing simple queries to fast small models like Gemini 2.5 Flash / GPT-4o-mini and complex queries to frontier reasoning models)?
4. How do you handle graceful degradation and fallback strategies when proprietary LLM APIs experience outages or rate limits (HTTP 429)?
5. How do you design streaming architectures (SSE / WebSockets) to provide instant Time-to-First-Token (TTFT) perceived latency to users?

---

## Enterprise-Scale AI System Design Problems
1. **Design an Enterprise Knowledge Base RAG System**:
   - Multi-tenant architecture with role-based access control (RBAC) at the document and chunk level.
   - Ingesting millions of documents (PDFs, Confluence, Google Drive, Notion) with asynchronous worker queues.
   - Hybrid search, cross-encoder reranking, and citation tracking back to source pages.
2. **Design an Autonomous Customer Support AI Agent**:
   - Multi-turn conversation state management and context window compaction.
   - Integration with enterprise APIs (order lookup, refunds, flight booking) with transactional guarantees and human escalation paths.
   - PII masking and sentiment-based routing.
3. **Design an AI Coding Assistant (Copilot / Cursor-like)**:
   - Ultra-low latency code completion (<150ms TTFT) using speculative decoding and local/edge models.
   - Whole-repository codebase indexing (AST parsing, ctags, embeddings).
   - Multi-file context retrieval and prompt construction for chat.
4. **Design a Real-Time Voice AI Conversational System**:
   - Speech-to-Text (STT - Whisper), LLM generation, and Text-to-Speech (TTS - ElevenLabs/Cartesia) pipeline.
   - Latency optimization: full duplex audio, handling user barge-in / interruptions, and token-to-speech streaming.
5. **Design a Document Extraction & Processing Pipeline (Multimodal RAG)**:
   - Extracting structured data from messy PDFs, scanned receipts, and tables.
   - Vision-Language Models (VLM) vs traditional OCR + LayoutLM vs table chunking strategies.
   - Human-in-the-loop review queue for low-confidence extractions.
