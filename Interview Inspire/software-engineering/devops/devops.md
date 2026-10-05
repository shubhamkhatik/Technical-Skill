# DevOps & Cloud Engineering Interview Questions

---

## Linux & Shell Fundamentals
1. How does the Linux process lifecycle work (fork, exec, zombie, orphan processes)?
2. How do you troubleshoot high CPU, high memory, or I/O bottlenecks on a Linux server (`top`, `htop`, `vmstat`, `iostat`, `strace`)?
3. What is the difference between hard links and soft (symbolic) links?
4. How do file permissions (chmod, chown, umask) and file descriptors (stdin, stdout, stderr) work in Unix?
5. How does `systemd` manage services, and how do you write a custom systemd service unit?

---

## Networking & Web Servers (Nginx, DNS, SSL/TLS, HTTP)
1. What happens during a DNS lookup from browser cache to authoritative name server?
2. What is the difference between TCP and UDP? Explain the TCP three-way handshake and four-way termination.
3. How does SSL/TLS handshake work (TLS 1.2 vs TLS 1.3), and how does HTTPS ensure both confidentiality and integrity?
4. How does Nginx work as a Reverse Proxy and Load Balancer? Explain round-robin, least-connections, and ip-hash algorithms.
5. What are the key performance improvements of HTTP/2 and HTTP/3 (QUIC) over HTTP/1.1?

---

## Containers & Docker
1. What is the underlying architecture of Docker (Linux namespaces, cgroups, Union File System / OverlayFS)?
2. What is the difference between a Virtual Machine (hypervisor) and a Docker Container?
3. How do you optimize a Dockerfile to minimize image size and build cache utilization (multi-stage builds, layer ordering)?
4. What is the difference between `CMD` and `ENTRYPOINT` in a Dockerfile?
5. How does Docker container networking work (bridge, host, overlay, none)?
6. How do Docker Volumes differ from Bind Mounts and `tmpfs`?

---

## Kubernetes (K8s) & Container Orchestration
1. What is the architecture of Kubernetes Control Plane (API Server, etcd, Scheduler, Controller Manager) vs Worker Nodes (kubelet, kube-proxy, container runtime)?
2. What is a Pod, and why does Kubernetes use Pods instead of running containers directly?
3. What is the difference between a Deployment, a StatefulSet, and a DaemonSet?
4. How do Kubernetes Services (ClusterIP, NodePort, LoadBalancer, ExternalName) route traffic to Pods?
5. What is the role of an Ingress Controller, and how does it differ from a LoadBalancer Service?
6. How does Horizontal Pod Autoscaler (HPA) scale pods based on CPU, memory, or custom Prometheus metrics?
7. What are ConfigMaps and Secrets, and how are they mounted into Pods safely?
8. What is the difference between Liveness, Readiness, and Startup Probes? What happens when each fails?

---

## CI/CD Pipelines & Deployment Strategies
1. What are the core stages of a modern CI/CD pipeline (Lint, Unit Test, Integration Test, Security Scan, Build, Deploy)?
2. What is the difference between Blue-Green Deployment, Canary Deployment, and Rolling Updates?
3. How do you implement zero-downtime database migrations in a continuous deployment environment?
4. How do you securely handle secrets and environment variables in GitHub Actions or GitLab CI?
5. What is GitOps, and how does ArgoCD / Flux automate deployments based on Git repository states?

---

## Cloud Infrastructure & Terraform (IaC)
1. What are the advantages of Infrastructure as Code (IaC) over manual console provisioning?
2. How does Terraform state management work? What is state drift, and why is remote state locking (S3 + DynamoDB) essential?
3. What is the difference between `terraform plan`, `terraform apply`, and `terraform refresh`?
4. How do you design a highly available multi-region architecture on AWS/GCP?
5. What is the difference between public, private, and isolated subnets in a VPC?

---

## Monitoring, Observability & Site Reliability (SRE)
1. What are the Three Pillars of Observability (Metrics, Logs, Traces)?
2. What are the Four Golden Signals in Site Reliability Engineering (Latency, Traffic, Errors, Saturation)?
3. What is the difference between SLI, SLO, and SLA? How do you calculate error budgets?
4. How does Prometheus pull metrics, and what are the 4 metric types (Counter, Gauge, Histogram, Summary)?
5. What is distributed tracing (OpenTelemetry / Jaeger), and how does context propagation work across microservices?