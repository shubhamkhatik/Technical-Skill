# System Design Interview Questions

---

## Core System Design Principles & Scalability
1. What is the difference between Vertical Scaling (Scaling Up) and Horizontal Scaling (Scaling Out)? What are the limits of each?
2. What are Latency vs Throughput, and Availability vs Consistency?
3. Explain the CAP Theorem and PACELC Theorem with real-world database examples.
4. What is the difference between Synchronous and Asynchronous communication? When should you use Event-Driven Architecture?
5. How do you estimate Back-of-the-envelope calculations (QPS, storage, bandwidth, memory requirements) during an interview?

---

## Load Balancing & Traffic Routing
1. What is the difference between Layer 4 (Transport) and Layer 7 (Application) Load Balancing?
2. How does Consistent Hashing work, and how does it prevent massive key remapping when adding or removing cache/database nodes?
3. How does DNS-based load balancing (GeoDNS, Anycast) route global users to the nearest data center?
4. What is an API Gateway, and what responsibilities should it handle (rate limiting, authentication, SSL termination, request routing)?

---

## Database Scaling, Sharding & Replication
1. What is Database Replication (Single-Leader, Multi-Leader, Leaderless)? What are the tradeoffs between synchronous and asynchronous replication?
2. What is Database Sharding (Horizontal Partitioning)? What are the strategies for choosing a good Shard Key?
3. What is the difference between Range-based Sharding, Directory-based Sharding, and Hash-based Sharding?
4. How do you handle Cross-Shard Queries and Distributed Transactions (2-Phase Commit vs SAGA Pattern)?
5. What is CQRS (Command Query Responsibility Segregation), and how does it optimize read-heavy systems?

---

## Caching & Content Delivery Networks (CDN)
1. Where can caching be applied in a full-stack system architecture (Browser, CDN, Reverse Proxy, Application Cache, Database Buffer Pool)?
2. How do CDNs cache static vs dynamic content using edge compute (Cloudflare Workers, AWS CloudFront)?
3. How do you design a distributed cache cluster (like Memcached or Redis Cluster) with high availability?
4. How do you handle cache invalidation at scale without introducing stale reads or thundering herds?

---

## Classic High-Level Design (HLD) Problems
1. **Design a URL Shortener (TinyURL / Bitly)**: Unique ID generation (Base62 vs Snowflake), high read-to-write ratio, redirect latency, cache strategy.
2. **Design a Distributed Rate Limiter**: Leaky bucket vs sliding window counter, Redis Lua scripts, handling race conditions across distributed nodes.
3. **Design a Social Media News Feed (Twitter / Instagram)**: Fanout-on-write (push) vs Fanout-on-read (pull) for celebrity accounts, hybrid architecture, ranking.
4. **Design a Chat & Messaging System (WhatsApp / Slack)**: WebSockets vs Long Polling, message ordering, delivery receipts (sent, delivered, read), group chat fanout, offline message storage.
5. **Design a Video Streaming Platform (YouTube / Netflix)**: Video chunking (HLS / DASH), adaptive bitrate streaming, transcoding pipeline, CDN distribution.
6. **Design an E-Commerce Flash Sale / Ticketing System (BookMyShow / Amazon)**: Concurrency control, distributed locks (Redlock), inventory countdown, preventing overselling.
7. **Design a Web Crawler**: Politeness policy, URL frontier, duplicate detection (Bloom filters), handling robots.txt.
8. **Design a Distributed Unique ID Generator (Twitter Snowflake)**: Timestamp, datacenter ID, machine ID, sequence number.

---

## Low-Level Design (LLD) & Object-Oriented Design
1. What are SOLID principles? Give a concrete code example of Dependency Inversion vs Interface Segregation.
2. What is the Factory Pattern vs Abstract Factory Pattern?
3. How do you implement a thread-safe Singleton pattern in your language of choice?
4. Explain the Strategy Pattern and how it eliminates nested `if-else` or `switch` statements.
5. Explain the Observer Pattern / Pub-Sub Pattern and its real-world implementation.
6. **Design a Parking Lot System**: UML class diagram, vehicle types, spot assignment algorithms, fee calculation strategy.
7. **Design an Elevator System**: Request dispatching algorithms (SCAN / LOOK), handling multiple cars.
8. **Design a Notification Service**: Pluggable notification channels (Email, SMS, Push), retry mechanism with exponential backoff.
