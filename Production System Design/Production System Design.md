# Production System Design

All production system design concepts fall into 4 buckets:

1. **Handle more users** → scaling
2. **Respond faster** → performance
3. **Survive failures** → reliability
4. **Control behavior safely** → release + observability

## Module 1: Traffic & Load Handling

| **Core Concept** | **The Real-World Problem** | **Production Solution (Node/AWS)** | **Failure Mode / Trade-off** |
| --- | --- | --- | --- |
| **Load Balancing & Horizontal Scaling** | 1 server crashes under a 10k user traffic spike. | Wrap Express app in Docker; run multiple replicas behind AWS ALB. | Breaks in-memory state; requires external session storage. |
| **Auto Scaling** | Paying for 100 idle containers at 3 AM. | AWS Auto Scaling Groups triggered by active connections, not just CPU. | Scaling takes time (pulling images); sudden spikes still cause downtime. |
| **Rate Limiting** | Abusive scripts spam and crash the Express API. | Distributed rate limiting using Redis (`rate-limit-redis`). | Redis becomes a Single Point of Failure (SPOF); adds latency. |
| **Backpressure** | Reading a 5GB S3 file into memory crashes Node (OOM). | Use Node.js Streams (`.pipe()`) to pause reading when the write buffer is full. | Adds complexity to simple I/O tasks. |

## Module 2: Performance Optimization

| **Core Concept** | **The Real-World Problem** | **Production Solution (Node/AWS)** | **Failure Mode / Trade-off** |
| --- | --- | --- | --- |
| **Caching (Cache-Aside)** | Complex PostgreSQL joins take 500ms and max out DB CPU. | Check Redis first. If miss, query DB, save to Redis with TTL, return data. | Cache invalidation; users seeing stale data after an update. |
| **Content Delivery Network (CDN)** | High latency for global users fetching static assets. | Push Next.js static bundles and images to Cloudflare / AWS CloudFront. | Accidentally caching authenticated/private API routes globally. |
| **Lazy Loading & Pagination** | DB returns 10,000 rows; Next.js bundle is 4MB. | Cursor-based pagination on backend; `next/dynamic` on frontend. | Cursor pagination is harder to implement than simple `OFFSET`. |
| **Compression** | Sending massive raw JSON blocks mobile networks. | Offload Brotli/Gzip compression to Nginx or AWS ALB. | Doing compression inside Node.js heavily blocks the event loop. |

## Module 3: Asynchronous Processing

| **Core Concept** | **The Real-World Problem** | **Production Solution (Node/AWS)** | **Failure Mode / Trade-off** |
| --- | --- | --- | --- |
| **Message Queues** | 5-second image resize blocks the Node event loop for everyone. | Return `202 Accepted`; push job to AWS SQS; process in background worker. | Worker crashes mid-job; requires Dead Letter Queues (DLQ) and ACKs. |
| **Pub/Sub (Event-Driven)** | Uploading a video triggers 4 separate microservices sequentially. | Publish `VideoUploaded` to SNS/Kafka; services process in parallel. | Eventual consistency; UI needs WebSockets to know when processing is done. |

## Module 4: System Reliability

| **Core Concept** | **The Real-World Problem** | **Production Solution (Node/AWS)** | **Failure Mode / Trade-off** |
| --- | --- | --- | --- |
| **Timeouts** | 3rd-party API hangs; Node connections pile up and crash. | Always use `AbortController` or Axios timeouts for external requests. | Choosing the right timeout window (too short = false failures). |
| **Retries & Backoff** | Instant retries act as a DDoS attack on struggling APIs. | Implement Exponential Backoff with Jitter (1s, 2.5s, 4.1s). | Delays the eventual failure response back to the client. |
| **Circuit Breaker** | Payment API is completely down; waiting for timeouts wastes CPU. | Use `opossum` to "open" the circuit and fail instantly for 30 seconds. | Requires careful tuning of failure thresholds and recovery windows. |

## Module 5: Security & Access Control

| **Core Concept** | **The Real-World Problem** | **Production Solution (Node/AWS)** | **Failure Mode / Trade-off** |
| --- | --- | --- | --- |
| **Authentication (JWT)** | Storing JWTs in `localStorage` leads to XSS theft. | Send short-lived JWTs in `httpOnly` cookies; store Refresh Tokens in DB. | Implementing secure token rotation and revocation is complex. |
| **Authorization (ABAC)** | User A modifies `projectId` in API payload to delete User B's project (IDOR). | Validate ownership against DB or embed resource IDs in the JWT payload. | Heavy DB lookups on every single protected API route. |
| **API Gateway & Edge Security** | Botnets brute-force the Express login endpoint. | AWS WAF blocks malicious IPs at the edge before hitting Docker. | Legitimate users getting blocked by overly aggressive WAF rules. |

## Module 6: Data & Database Scaling

| **Core Concept** | **The Real-World Problem** | **Production Solution (Node/AWS)** | **Failure Mode / Trade-off** |
| --- | --- | --- | --- |
| **Replication (Read/Write Split)** | Single DB cannot handle the volume of `SELECT` queries. | Route `INSERT/UPDATE` to Primary DB, route `SELECT` to Read Replicas via Prisma. | Replication lag; users refresh page and see old data. |
| **Database Indexing** | Query scans 5 million rows ($O(N)$), taking 8 seconds. | Create B-Tree indexes on heavily queried columns. | Indexes consume RAM and significantly slow down write operations. |
| **Sharding** | Data size exceeds the physical limits of a single AWS RDS instance. | Horizontally partition data across multiple DBs using a Shard Key (e.g., `tenantId`). | Cross-shard joins become practically impossible. |

## Module 7: Deployment & Release Strategies

| **Core Concept** | **The Real-World Problem** | **Production Solution (Node/AWS)** | **Failure Mode / Trade-off** |
| --- | --- | --- | --- |
| **Rolling Deployment** | Restarting all containers at once causes downtime. | Orchestrator replaces old containers with new ones gradually. | Mixed versions: v1 and v2 running simultaneously breaks API contracts. |
| **Blue-Green Deployment** | Need instant zero-downtime rollbacks if a release fails. | Deploy to isolated "Green" environment; flip ALB traffic 100% instantly. | DB migrations running on Green can crash the live Blue environment. |
| **Canary Release** | Pushing a hidden bug to 100% of users. | Route 5% of traffic to the new version; monitor errors; ramp up to 100%. | Requires sticky sessions to prevent users bouncing between versions. |

## Module 8: Observability

| **Core Concept** | **The Real-World Problem** | **Production Solution (Node/AWS)** | **Failure Mode / Trade-off** |
| --- | --- | --- | --- |
| **Structured Logging** | `console.log` is impossible to search across 20 containers. | Use `pino` to write JSON logs; centralize in AWS CloudWatch / Datadog. | Logging full request objects causes OOM errors and high cloud bills. |
| **Monitoring & Metrics** | Need to alert the team when API error rate crosses 2%. | Expose `/metrics` endpoint; scrape with Prometheus; visualize in Grafana. | Cardinality explosion (tagging metrics with raw dynamic URLs crashes Prometheus). |
| **Distributed Tracing** | Request spans Next.js -> Express -> Postgres. Which part is slow? | Pass OpenTelemetry `Trace IDs` in HTTP headers across all services. | High setup complexity and performance overhead on massive scale. |

## Module 9: API & Communication Design

| **Core Concept** | **The Real-World Problem** | **Production Solution (Node/AWS)** | **Failure Mode / Trade-off** |
| --- | --- | --- | --- |
| **REST vs GraphQL** | Next.js over-fetches data, or makes 5 sequential REST calls (Waterfall). | Use Apollo GraphQL to request exact data shapes in a single network trip. | The N+1 Query Problem requires strict use of DataLoaders. |
| **Idempotency** | User clicks "Pay" twice; Express charges them twice. | Require an `Idempotency-Key` header; cache successful responses in Redis. | Redis cache eviction could technically allow a retry to slip through later. |
| **API Versioning** | Changing a payload shape breaks older mobile app clients. | URL versioning (`/v1/users`) or Header versioning (`Accept-Version`). | Maintaining multiple versions of business logic creates massive technical debt. |

## Module 10: Concurrency & Execution

| **Core Concept** | **The Real-World Problem** | **Production Solution (Node/AWS)** | **Failure Mode / Trade-off** |
| --- | --- | --- | --- |
| **Async Interleaving** | Node pauses on `await db`, processes another request, causing a race condition. | Push concurrency control to Postgres using atomic `UPDATE ... WHERE` queries. | Developers falsely assuming Node's single thread prevents race conditions. |
| **Distributed Locks** | 2 scaled containers receive duplicate webhooks and process both. | Use Redis Redlock (`SET ... NX EX`) so only one container claims the job. | Redis network blips can cause lock acquisition failures. |
| **Worker Threads** | Parsing a 50MB JSON object blocks the Node event loop for 800ms. | Offload CPU-heavy math/parsing to a `worker_threads` pool (e.g., `piscina`). | Thread creation is expensive; must maintain a persistent pool. |

## Module 11: Architecture Patterns

| **Core Concept** | **The Real-World Problem** | **Production Solution (Node/AWS)** | **Failure Mode / Trade-off** |
| --- | --- | --- | --- |
| **Monolith vs Microservices** | 50 devs working on one Express app block each other's deployments. | Split by domain context; communicate asynchronously via queues/events. | The "Distributed Monolith": services tied together by synchronous HTTP calls. |
| **API Gateway** | Exposing 15 internal microservices directly to the public internet. | Place AWS API Gateway at the edge to handle Auth, routing, and rate limiting. | The Gateway becomes a bottleneck if it handles heavy business logic. |
| **BFF (Backend for Frontend)** | Mobile app and Next.js web app need completely different data shapes. | Build separate API aggregation layers (e.g., Next.js API routes) for each client. | Duplication of routing and data aggregation logic across different BFFs. |

## Module 12: State Management at Scale

| **Core Concept** | **The Real-World Problem** | **Production Solution (Node/AWS)** | **Failure Mode / Trade-off** |
| --- | --- | --- | --- |
| **Stateless Services** | "Ghost logouts" when load balancer routes user to a different container. | Never store session data in Node memory. Store in Redis, pass ID via cookie. | Requires an extra network hop to Redis on every authenticated request. |
| **Sticky Sessions** | Legacy code requires persistent state on a specific server. | Configure AWS ALB to route specific users to the exact same container. | Uneven load distribution; deploying code destroys the users' sessions. |

## Module 13: Experimentation & Product Systems

| **Core Concept** | **The Real-World Problem** | **Production Solution (Node/AWS)** | **Failure Mode / Trade-off** |
| --- | --- | --- | --- |
| **Feature Flags** | Cannot safely test a new Checkout UI in production. | Evaluate feature flags on the server (Next.js Middleware) before rendering. | Evaluating flags on the client-side causes UI flickering (FOOC). |
| **A/B Testing** | Need deterministic splits without querying the database. | Use hashing (`murmurhash(userId) % 100`) to assign experiment groups. | Hash collisions if the salt/experiment keys are not unique. |
| **Analytics Pipelines** | Writing 500,000 analytics events/minute crashes the PostgreSQL DB. | Ingest to Kafka/Kinesis -> batch write to Data Warehouse (Redshift/BigQuery). | Analytics data is slightly delayed (Eventual Consistency) for Product Managers. |

## Module 14: Failure & Edge Case Thinking

| **Core Concept** | **The Real-World Problem** | **Production Solution (Node/AWS)** | **Failure Mode / Trade-off** |
| --- | --- | --- | --- |
| **DB Down / Partial Failure** | Primary DB goes offline; all API writes fail. | Accept the request, queue it in AWS SQS, and write it when DB recovers. | User UI shows success, but data isn't strictly saved yet. |
| **Distributed Transactions** | Order created, but Payment fails across microservices. | Implement the Saga Pattern (publish compensating "Undo" events). | Extremely complex to debug and trace across multiple services. |
| **Data Inconsistency** | Stripe says "Paid", but Postgres says "Pending" due to a dropped packet. | Build nightly asynchronous reconciliation cron jobs to self-heal data. | Requires maintaining separate scripts specifically for data auditing. |

## Module 15: Infrastructure as Code (IaC) & GitOps

| **Core Concept** | **The Real-World Problem** | **Production Solution (Node/AWS)** | **Failure Mode / Trade-off** |
| --- | --- | --- | --- |
| **Infrastructure Automation** | Manual AWS Console changes cause untrackable, unrepeatable outages. | Define AWS resources in Terraform/AWS CDK; deploy via GitHub Actions. | High learning curve; manual changes made outside IaC cause state drift. |
| **Immutable Infrastructure** | SSH-ing into a container to fix a bug works, but gets wiped on auto-scale. | Never modify running servers. Update the code, build a new Docker image, redeploy. | Slower to apply emergency hotfixes (requires running the full CI/CD pipeline). |

## Module 16: Disaster Recovery (DR) & Human Error Prevention

| **Core Concept** | **The Real-World Problem** | **Production Solution (Node/AWS)** | **Failure Mode / Trade-off** |
| --- | --- | --- | --- |
| **Point-in-Time Recovery (PITR)** | Dev runs `DROP TABLE users`; replicas copy the deletion instantly. | Configure Postgres continuous backups to restore to a specific minute in time. | Restoring a multi-TB database from S3 backups takes significant time (High RTO). |
| **Soft Deletes** | Deleting a user cascades and breaks historical analytics data. | Add `deletedAt` timestamp in Prisma; never hard-delete production data. | Queries become complex (must always append `WHERE deletedAt IS NULL`). |

## Module 17: FinOps (Cost-Aware Architecture)

| **Core Concept** | **The Real-World Problem** | **Production Solution (Node/AWS)** | **Failure Mode / Trade-off** |
| --- | --- | --- | --- |
| **Auto-scaling Limits** | Infinite scaling during an attack results in a $40k AWS bill (EDoS). | Set hard maximum limits on AWS Auto Scaling Groups. | The system will degrade and drop traffic when the hard limit is reached. |
| **Data Lifecycle Policies** | Paying premium S3 prices for millions of old, unused user avatars. | Configure S3 to automatically move files >30 days old to Glacier storage. | Retrieving data from Glacier takes hours; breaks instant UI access. |