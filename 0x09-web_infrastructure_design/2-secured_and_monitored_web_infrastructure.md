# ALX PROJECT

## 0X09 Web Infrastructure Design

### Task 2 – Secured and Monitored Web Infrastructure

Explanations of the infrastructure in the task;

1. **For every additional element, why are we adding it**: Here, we have added three new components; a firewall for each server to protect them from being attacked and exploited, 1 SSL certificate to server `www.foobar.com` over HTTPS ensuring data confidentiality and integrity and three monitoring clients that will collect logs and metrics from servers, aiding in proactive monitoring and analysis and send them to our data collector Sumologic.

2. **What are firewalls for**: Firewall is a network security system that monitors and controls incoming and outgoing network traffic based on predetermined security rules. It basically establishes a barrier between a trusted network and an untrusted one.

3. **Why is the traffic served over HTTPS**: Traffic is served over HTTPS to encrypt data in transit. HTTPS ensures the confidentiality and integrity of data exchanged between users and the web server. It prevents eavesdropping and data tampering, providing a secure communication channel.

4. **What monitoring is used for**: Monitoring is used for security, performance tracking, and issue troubleshooting. It allows for proactive identification of security threats, ensures optimal server performance by tracking metrics, and aids in rapid issue identification and resolution.

5. **How the monitoring tool is collecting data**: The Sumologic monitoring client collects and sends logs to the monitoring service. Sumologic aggregates logs and metrics from servers, providing a centralized platform for analysis. This data collection facilitates real-time monitoring, anomaly detection, and effective troubleshooting.

6. **Explain what to do if you want to monitor your web server QPS**: Procedure: To monitor our web server QPS (Queries Per Second):

- We can utilize monitoring tools to track server metrics, including the number of incoming queries per second.
- Set up alerts to notify us when QPS exceeds predefined thresholds.
- Analyze the data to identify patterns, spikes, or potential performance bottlenecks.
- Adjust server resources or configurations as needed to optimize QPS.

Issues with this infrastructure:

i. **SSL Termination at Load Balancer**: This setup exposes decrypted traffic within the internal network. We can consider end-to-end encryption for enhanced security.

ii. **Why having only one MySQL server capable of accepting writes is an issue**: A single point of failure for write operations. Implement database clustering for redundancy.

iii. **Identical Server Components**: Uniformity might lead to common vulnerabilities (bugs, etc.). Introduce diversity in components to reduce the risk of widespread issues.
