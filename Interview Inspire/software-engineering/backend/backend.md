# Backend Engineering Interview Questions

---

## API Design & Architecture (REST, GraphQL, gRPC)
1. **[Core Concept]** What are the key principles of RESTful API design, and what makes an API truly idempotent?
2. **[Core Concept]** What are the differences between REST, GraphQL, and gRPC? When would you choose one over the others?
3. **[Core Concept]** How do you design and implement API rate limiting (Token Bucket vs Leaky Bucket vs Fixed/Sliding Window)?
4. **[Core Concept]** What is the difference between WebSockets, Server-Sent Events (SSE), and Long Polling? What are the use cases for each?
5. **[Core Concept]** How do you handle API versioning (URI path, query params, headers), and how do you deprecate old versions gracefully?
6. **[Technical Deep Dive]** How do you prevent and mitigate the N+1 query problem in GraphQL?
7. **[Core Concept]** What are HTTP status codes 401 vs 403, and 502 vs 504?
8. **[Technical Deep Dive]** How do you implement distributed API rate limiting across multi-server clusters using Redis and Lua scripts to prevent race conditions between read and increment?

---

## Relational Databases (SQL & PostgreSQL/MySQL)
1. **[Core Concept]** What are ACID properties in relational databases? Explain how transactions ensure consistency.
2. **[Technical Deep Dive]** What are Database Isolation Levels (Read Uncommitted, Read Committed, Repeatable Read, Serializable) and the anomalies they prevent (Dirty reads, Non-repeatable reads, Phantom reads)?
3. **[Technical Deep Dive]** How do B-Tree and B+Tree indexes work internally? When does a database decide to use or ignore an index?
4. **[Core Concept]** What is the difference between Clustered and Non-Clustered indexes?
5. **[Technical Deep Dive]** What are Composite Indexes, and how does the leftmost prefix rule affect query performance?
6. **[Technical Deep Dive]** How do you analyze and optimize a slow-running SQL query using `EXPLAIN ANALYZE`?
7. **[Technical Deep Dive]** What is Database Connection Pooling, and why is it critical in high-traffic applications?
8. **[Core Concept]** When should you normalize vs denormalize a relational database schema?

---

## NoSQL & Key-Value Stores (MongoDB, Redis, DynamoDB)
1. **[Core Concept]** What is the CAP theorem, and where do MongoDB, Cassandra, and DynamoDB fall within it?
2. **[Core Concept]** What is the difference between Document, Key-Value, Columnar, and Graph databases?
3. **[Technical Deep Dive]** How does DynamoDB achieve horizontal scaling and single-digit millisecond latency? What are Partition Keys and Sort Keys?
4. **[Core Concept]** What is Eventual Consistency vs Strong Consistency in distributed databases?
5. **[Core Concept]** When should you choose a NoSQL database over a Relational database (and vice-versa)?

---

## Caching Strategies & Redis
1. **[Core Concept]** What are the most common caching patterns: Cache-Aside, Write-Through, Write-Around, and Write-Back?
2. **[Technical Deep Dive]** How do you handle Cache Invalidation? What is the Cache Stampede (Thundering Herd) problem and how do you prevent it?
3. **[Technical Deep Dive]** What is the difference between Cache Penetration, Cache Breakdown, and Cache Avalanche? How do Bloom Filters help?
4. **[Core Concept]** What eviction policies does Redis support (LRU, LFU, TTL, Random)?
5. **[Technical Deep Dive]** How does Redis achieve high throughput despite being single-threaded for command execution?
6. **[Core Concept]** What data structures does Redis support beyond simple strings (Hashes, Sets, Sorted Sets, HyperLogLog, Bitmaps)?
7. **[System Design]** In high-traffic systems, how do you architect Redis across diverse use cases (in-memory caching vs distributed session stores vs Pub/Sub messaging vs distributed locks with Redlock)?
8. **[Technical Deep Dive]** How do you prevent Cache Stampede (Thundering Herd) when high-concurrency keys expire using distributed mutex locks (`SETNX`) or probabilistic early expiration (XFetch algorithm)?

---

## Message Brokers & Event-Driven Architecture (Kafka, RabbitMQ)
1. **[Core Concept]** What is the difference between a Message Queue (RabbitMQ) and an Event Streaming Platform (Apache Kafka)?
2. **[Technical Deep Dive]** How does Apache Kafka ensure ordered message processing across partitions?
3. **[Technical Deep Dive]** What are Consumer Groups in Kafka, and what triggers a partition rebalance?
4. **[Technical Deep Dive]** How do you achieve Exactly-Once Semantics (EOS) or idempotent message processing in distributed systems?
5. **[Core Concept]** What is a Dead Letter Queue (DLQ), and how should poison pill messages be handled?
6. **[Technical Deep Dive]** What is the Outbox Pattern, and how does it guarantee dual-write consistency between a database and a message broker?

---

## Authentication, Authorization & Security
1. **[Core Concept]** What is the difference between Authentication (AuthN) and Authorization (AuthZ)?
2. **[Technical Deep Dive]** How does JSON Web Token (JWT) work? What are the security risks of storing sensitive data or refresh tokens in `localStorage` vs `HttpOnly` cookies?
3. **[Technical Deep Dive]** What are OAuth 2.0 and OpenID Connect (OIDC)? Explain the Authorization Code Grant with PKCE flow.
4. **[Core Concept]** What is Role-Based Access Control (RBAC) vs Attribute-Based Access Control (ABAC)?
5. **[Technical Deep Dive]** How do you protect backend APIs against SQL Injection, Cross-Site Scripting (XSS), and Cross-Site Request Forgery (CSRF)?
6. **[Technical Deep Dive]** How should user passwords be hashed and salted (bcrypt, Argon2, PBKDF2)?
7. **[Technical Deep Dive]** In a React + Node.js application, what layers of defense protect against XSS, CSRF, and prototype pollution, and why should refresh tokens be stored strictly in `HttpOnly`, `Secure`, `SameSite=Strict` cookies?

---

## Concurrency, Threading & Performance
1. **[Core Concept]** How does Node.js handle high concurrency with a single-threaded event loop compared to multi-threaded runtimes (Java/Go)?
2. **[Core Concept]** What is the difference between CPU-bound tasks and I/O-bound tasks? How do you offload CPU-bound tasks in Node or Python?
3. **[Technical Deep Dive]** What are Race Conditions and Deadlocks? How do optimistic locking vs pessimistic locking solve data conflicts?
4. **[Technical Deep Dive]** What is a Circuit Breaker pattern, and how does it prevent cascading failures in microservices?
5. **[Technical Deep Dive]** How do you profile memory leaks and CPU bottlenecks in backend services?
