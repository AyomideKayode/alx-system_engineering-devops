# ALX PROJECT.

## 0X09 Web Infrastructure Design.

### Task 0 – Simple Web Stack:

Explanations of the infrastructure in the task;

1. **What is a Server**: A server is a device, a virtual device or computer program providing functionality for other programs or devices, called “clients”.
2. **What is the role of a domain name**: The domain name serves as to identify internet resources, such as computers, networks, and services with a text-based label that is easier to memorize than number-based addresses (IP addresses).
3. **What type of DNS record `www` is in `www.foobar.com`**: This is a CNAME (Canonical Name) record pointing www to the domain.
4. **What is the role of the Web Server**: The role of the web server is to store, process and display website contents (codebase); deliver web pages to users (basically HTML and CSS) over the protocol HTTP. It basically handles incoming HTTP requests, manages static content, and forwards dynamic requests to the application server.
5. **What is the role of the Application Server**: The role of the application server is to execute server-side code (JSP, Ajax, PHP, etc.) and generate dynamic content based on user requests.
6. **What is the role of the Database**: The role of the database is to manage data systematically and efficiently in a well-organized manner which allows data to be easily added, accessed, updated, managed and deleted.
7. **What is the server using to communicate with the computer of the user requesting the website**: The server communicates through HTTP protocol.

Issues with this infrastructure:

i. **SPOF (Single Point of Failure)**: Firstly, a SPOF is a system that if any component fails, the entire system goes down. So having a server that contains only one web server, application server, and database will result in a lot of single point of failure.

ii. **Downtime when maintenance needed (like deploying new code web server needs to be restarted)**: Necessary maintenance which would warrant downtime period might be longer than expected due to the fact that our server is dependent on one codebase which is unavailable at the moment. Users will therefore not be able to access the website and its contents which results in a bad user experience and traffic. We might consider implementing strategies like load-balancing to minimize impact.

iii. **Cannot scale if too much incoming traffic**: A single server may struggle with increased traffic. Since the domain name points directly at the server hence does not contain a load balancer which allows handling increased loads easier. An alternative might be to set a limit to the number of users the website will be able to accommodate.
