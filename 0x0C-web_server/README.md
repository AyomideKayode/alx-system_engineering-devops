# Project: 0x0C. Web server

## Resources

### Read or watch :-

- [How the web works](https://developer.mozilla.org/en-US/docs/Learn/Getting_started_with_the_web/How_the_Web_works)
- [Nginx](https://en.wikipedia.org/wiki/Nginx)
- [How to Configure Nginx](https://www.digitalocean.com/community/tutorials/how-to-set-up-nginx-server-blocks-virtual-hosts-on-ubuntu-16-04)
- [Child process concept page](./child_process_concept.md)
- [Root and sub domain](https://landingi.com/help/domains-vs-subdomains/)
- [HTTP requests](https://www.tutorialspoint.com/http/http_methods.htm)
- [HTTP redirection](https://moz.com/learn/seo/redirection)
- [Not found HTTP response code](https://en.wikipedia.org/wiki/HTTP_404)
- [Logs files on Linux](https://www.cyberciti.biz/faq/ubuntu-linux-gnome-system-log-viewer/)

### For reference :-

- [RFC 7231 (HTTP/1.1)](https://datatracker.ietf.org/doc/html/rfc7231)
- [RFC 7540 (HTTP/2)](https://datatracker.ietf.org/doc/html/rfc7540)

### man or help

- `scp`
- `curl`

## Learning Objectives

### General

- What is the main role of a web server
- What is a child process
- Why web servers usually have a parent process and child processes
- What are the main HTTP requests

## Tasks

0. [Transfer a file to your server](./0-transfer_file):

Write a Bash script that transfers a file from our client to a server:

Requirements:

- Accepts 4 parameters
  1. The path to the file to be transferred
  2. The IP of the server we want to transfer the file to
  3. The username scp connects with
  4. The path to the SSH private key that scp uses
- Display `Usage: 0-transfer_file PATH_TO_FILE IP USERNAME PATH_TO_SSH_KEY` if less than 3 parameters passed
- scp must transfer the file to the user home directory `~/`
- Strict host key checking must be disabled when using `scp`

Example:

```sh
sylvain@ubuntu$ ./0-transfer_file
Usage: 0-transfer_file PATH_TO_FILE IP USERNAME PATH_TO_SSH_KEY
sylvain@ubuntu$
sylvain@ubuntu$ ssh ubuntu@8.8.8.8 -i /vagrant/sylvain 'ls ~/'
afile
sylvain@ubuntu$ 
sylvain@ubuntu$ touch some_page.html
sylvain@ubuntu$ ./0-transfer_file some_page.html 8.8.8.8 sylvain /vagrant/private_key
some_page.html                                     100%   12     0.1KB/s   00:00
sylvain@ubuntu$ ssh ubuntu@8.8.8.8 -i /vagrant/private_key 'ls ~/'
afile
some_page.html
sylvain@ubuntu$
```

In this example, I:

- remotely execute the ls ~/ command via ssh to see what ~/ contains
- create a file named some_page.html
- execute my 0-transfer_file script
- remotely execute the ls ~/ command via ssh to see that the file `some_page.html` has been successfully transferred

That is one way of publishing your website pages to your server.

| Task                              | File                                                       |
| --------------------------------- | ---------------------------------------------------------- |
|                        |
| 1. Install nginx web server       | [1-install_nginx_web_server](./1-install_nginx_web_server) |
| 2. Setup a domain name            | [2-setup_a_domain_name](./2-setup_a_domain_name)           |
| 3. Redirection                    | [3-redirection](./3-redirection)                           |
| 4. Not found page 404             | [4-not_found_page_404](./4-not_found_page_404)             |
