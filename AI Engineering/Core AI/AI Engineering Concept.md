

### Vector Embeddings

Vector embeddings convert real-world content, like documents and images, into 1-D numerical
representations (arrays).
These arrays have N values, representing N dimensions. They are called vectors and can be
compared with each other efficiently.
These vectors aren’t random blobs of numbers. They live in a semantic multi-dimensional
space, and their position encodes real meaning.

Key Takeaways
● Vector embeddings = position in a multi-dimensional space.
● Each axis can be thought of as representing a property: realism, length, time, and
popularity.
● Similar vectors = semantically similar content.
● Clusters = emergent structure from data, not hard-coded.

---

### Compression & Quantization

1. Product Quantization (PQ)
● Break each vector into sub-vectors (e.g., split a 128D vector into 8 chunks of 16D).
● For each chunk, find the nearest centroid from a pre-trained codebook                                ● Store only the index of the centroid, not the float values.
So instead of storing 128 floats (512 bytes), you store 8 integers (8 bytes).
That’s a 64x reduction.
PQ is used heavily in Facebook's FAISS, Milvus, and other modern vector DBs.
2. Scalar Quantization (SQ)
● Compress each float in the vector individually.
● Convert from 32-bit float to 8-bit (or less) integer using fixed scale and offset.
This is simpler than PQ but less precise. Often combined with vector normalization

Key Takeaways
● Vector compression allows fast, scalable search.
● PQ: Sub-vector + codebook trick (most powerful).
● SQ: Per-float quantization.
● INT8: Hardware-friendly, model-compatible.
● Always balance: size vs recall vs latency.

---

### Search Execution Flow: From Query to Result

Step 1: Embed the Query

Step 2: Search the Index

 we use ANN (Approximate Nearest Neighbor) indexes like IVF and HNSW.

Step 3: Score & Rank
For each candidate vector from the index, compute a similarity score using either:

1. L2 distance (Euclidean)
2. Cosine similarity
3. Dot product (less common)
Then return the top-K closest vectors. Cosine similarity is usually preferred for textual
embeddings since it's scale-invariant

Step 4: Post-processing & Filtering
Now you apply filters if needed:
● Language = English
● Published after 2023
● Category = Product Manual
Metadata filters are applied after vector scoring.

The vector search flow is
Query → Embedding → Index Search → Distance Score → Top-K → Filter Result

#### Indexing Techniques for Vector Search

1. IVF – Inverted File Index
Cluster the vector space into regions using K-Means. At query time, find the nearest cluster
centroids, then only scan vectors within those clusters

Tunable parameters:
● Number of clusters
● Number of clusters to search at runtime
Trade-off:
Lots of clusters → better recall and slower search.
Few clusters → fast, less accurate search.
Very large number of clusters → Slow, brittle recommendations.
Very few clusters → Full table scan

1. HNSW – Hierarchical Navigable Small World Graph
A. Build a graph where nodes are vectors and edges connect to “close” vectors.
B. The graph has multiple levels: The Top levels are sparse, the lower ones are dense.
C. During construction, nodes with a high degree (highly connected nodes) are chosen to
be promoted to an upper layer. This is done recursively, till a few nodes are on the top
layer.
D. Search is like climbing down a mountain: Start high, zoom into the nearest zones layer
by layer.


Why don’t we use QuadTrees or R-Trees?
Because they work well for 2D or 3D. But in a 100D+ vector space, they suffer from the curse of
dimensionality. The space becomes too sparse, and partitioning doesn’t help.
Key takeaways
● Indexing makes vector search practical at scale.
● IVF splits the vector space into clusters.
● HNSW builds a graph and uses multi-level traversal

---

### How to Reduce Hallucinations

1. Ground the Prompt with Facts
○ Use Retrieval-Augmented Generation (RAG) to feed in real documents.
○ Add inline citations or structured constraints in the system prompt.
2. Reduce Prompt Scope
○ Don’t stuff 20 documents into every query.
○ Input the top 2–3 most relevant chunks.
○ Smaller prompt = sharper context = less drift

3. Force Answer Shape
○ Use few-shot prompting (examples).
○ Add instructions like "Answer only based on the documents provided. Do not
speculate."
○ Use reusable templates:
"You are a support assistant. Use the provided context to
answer..."
4. Retrieval Augmented Generation (RAG)
○ Select documents most relevant to a query based on vector search.
○ Use the documents to augment the original query.
5. Guardrails & Validation
○ Post-process with rules: “If it says ‘7 days’, check against actual policy.”
○ Use LLM output as a draft → validate using code

---

### LLM Optimization technique

Key Takeaways
● Attention helps a model understand what matters and how words relate to each other.
● KV caching helps the model do this efficiently, especially when generating longer texts

KV Caching  + Mixture of Experts (MoE) +  Paged Attention + Flash Attention 

---

**Tradeoffs in LLMs**

**Quantization + Sparse Attention + SLM and Distillation + Speculative Decoding**

---

**Context Injection** feeds the AI the *facts* it needs to know, while **Chain of Thought** guides the AI through the *logical steps* it must take to process those facts