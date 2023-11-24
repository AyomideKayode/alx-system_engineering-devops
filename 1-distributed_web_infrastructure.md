# ALX PROJECT.

## 0X09 Web Infrastructure Design.

### Task 1 – Distributed Web Infrastructure:

Explanations of the infrastructure in the task;

1. **For every additional element, why are we adding it**: Additional servers are added for redundancy, load balancing and improved performance. And also to enable us eliminate a single point of failure which could occur by having a single server.

2. **What distribution algorithm your load balancer is configured with and how it works**: HA Proxy Load Balancer. Distributes traffic evenly between the application servers, ensuring efficient resource utilization and high availability.

- Distribution Algorithm: Configured with a round-robin algorithm, directing requests sequentially to each server.

3. **Is your load-balancer enabling an Active-Active or Active-Passive setup, explain the difference between both**:
- **`Active-Active Setup`**: Both application servers actively handle requests, improving system reliability and performance.
- **`Active-Passive Setup`**: One server is active while the second stands by to handle requests that the current server might delegate.
- Key difference between the two is performance. Active-Active gives access to the resources of all your servers during a normal operation. While in an Active-Passive cluster, the backup/standby server only sees action during failover.
4. **How a database Primary-Replica (Master-Slave) cluster works**: Master-Slave replication enables data from one database server (the master) to be replicated to one or more other database servers (the slaves). The master logs the updates, which then ripples through the slaves. If the changes are made to the master and slave at the same time, it is synchronous. If changes are queued up and written later, it is asynchronous. It is usually used to spread read access on multiple servers for scalability, although it can also be used for other purposes such as failover, or analyzing data on the slave in order not to overload the master.

5. **What is the difference between the Primary node and the Replica node in regard to the application**: 
- **`Primary Node`**: Handles write operations and serves as the authoritative source for data.
- **`Replica Node`**: Mirrors data from the primary node, serving read-only operations and enhancing read scalability. Provides redundant copies of the application codebase to protect against hardware failure and increase capacity to serve read requests like searching or retrieving a document.

Issues with this infrastructure:

i. **SPOF (Single Point of Failure)**: The load balancer could be a potential SPOF. We could consider adding redundancy or a failover mechanism.

ii. **Security Issues**: Lack of firewall and HTTPS poses security risks. We should implement firewalls and enable HTTPS to secure data in transit.

iii. **Monitoring**: Absence of monitoring tools makes it challenging to identify and address performance issues. Integrate monitoring solutions for proactive management.
