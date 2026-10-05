# LLM & RAG Interview Questions

---

## Large Language Models (LLM) Fundamentals
1. What is the pre-training objective of modern decoder-only LLMs (Causal Language Modeling / Next Token Prediction)?
2. What are Temperature, Top-K, Top-P (Nucleus Sampling), and Repetition Penalty? How do they affect output diversity and determinism?
3. What is the KV Cache in Transformer inference? How does it save redundant computation during autoregressive generation?
4. What is the Context Window, and what challenges arise with "needle-in-a-haystack" retrieval as context lengths grow to 1M+ tokens?
5. What are the key stages of training an LLM: Pre-training, Supervised Fine-Tuning (SFT), and Alignment (RLHF / DPO)?

---

## Prompt Engineering & In-Context Learning
1. What is the difference between Zero-Shot, Few-Shot, and Many-Shot Prompting?
2. Explain Chain-of-Thought (CoT), Tree of Thoughts (ToT), and Self-Consistency prompting.
3. How do you guarantee Structured Outputs (JSON Schema, Pydantic, Instructor, Outlines) from an LLM?
4. What is Prompt Injection (Direct vs Indirect)? How do you protect LLM systems from jailbreaks and data exfiltration?
5. How do system instructions differ from user messages in Chat Markup Language (ChatML) templates?

---

## Embeddings & Vector Databases
1. What are Text Embeddings? How do dense embeddings (e.g. OpenAI text-embedding-3, BGE) differ from sparse embeddings (BM25 / SPLADE)?
2. What are the differences between Cosine Similarity, Dot Product, and Euclidean (L2) Distance? When are they equivalent?
3. What is an Approximate Nearest Neighbor (ANN) index? How does HNSW (Hierarchical Navigable Small World) balance recall and search latency?
4. What is Product Quantization (IVF-PQ) and how does it compress vector dimensions to fit millions of vectors in memory?
5. What are the pros and cons of dedicated vector databases (Pinecone, Qdrant, Milvus, Chroma) vs relational extensions like `pgvector`?

---

## Retrieval-Augmented Generation (RAG) Architecture
1. What is Naive RAG vs Advanced RAG vs Modular RAG? What are the primary failure points of Naive RAG?
2. What are the trade-offs of different Chunking Strategies (Fixed-size with overlap, Recursive character, Markdown/HTML header-aware, Semantic chunking)?
3. What is Hybrid Search, and how does Reciprocal Rank Fusion (RRF) combine dense semantic search with sparse keyword search?
4. What is Re-ranking (Cross-Encoders, Cohere Rerank, BGE-Reranker)? Why is a two-stage retrieval (Bi-encoder candidate generation + Cross-encoder reranking) the industry standard?
5. What is Query Transformation (Query Expansion, Multi-Query, Step-Back Prompting, HyDE - Hypothetical Document Embeddings)?
6. How do you solve the "Lost in the Middle" problem in long context retrieval?
7. What is Parent-Document Retrieval (Sentence-window retrieval), and how does it decouple the chunk used for embedding from the chunk passed to the LLM?
