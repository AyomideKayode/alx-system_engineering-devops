# Project: 0x1A. Application server

![application_server-img](./technicals/application_server.jpg)

## Resources

#### Read or watch:

- [Application server vs web server](https://intranet.alxswe.com/rltoken/B9fOBzIxX_t1289WAuRzJw)
- [How to Serve a Flask Application with Gunicorn and Nginx on Ubuntu 16.04](https://intranet.alxswe.com/rltoken/kpG6RwmwRJHzRmGUM_ERcA)
- [Running Gunicorn](https://intranet.alxswe.com/rltoken/2LF1j7xKJGYaUtD1HKgUeQ)
- [Be careful with the way Flask manages slash](https://intranet.alxswe.com/rltoken/lEg0zpkkDcLtdl3VD4ACRQ)
- [Upstart documentation](https://intranet.alxswe.com/rltoken/cldrneY3Qr7LlDysygzRHw)

## Tasks

0. [Set up development with Python](./README.md) :

Let’s serve what you built for [AirBnB clone v2 - Web framework](https://github.com/AyomideKayode/AirBnB_clone_v2/tree/master/web_flask) on `web-01`. This task is an exercise in setting up your development environment, which is used for testing and debugging your code before deploying it to production.

Requirements:

- Make sure that [task #3](../0x0B-ssh/README.md) of your [SSH project](../0x0B-ssh/) is completed for `web-01`. The checker will connect to your servers.
- Install the `net-tools` package on your server: `sudo apt install -y net-tools`
- Git clone your `AirBnB_clone_v2` on your `web-01` server.
- Configure the file `web_flask/0-hello_route.py` to serve its content from the route `/airbnb-onepage/` on port `5000`.
- Your Flask application object must be named `app` (This will allow us to run and check your code).

Example:

Window 1:

```sh
ubuntu@229-web-01:~/AirBnB_clone_v2$ python3 -m web_flask.0-hello_route
 * Serving Flask app "0-hello_route" (lazy loading)
 * Environment: production
   WARNING: Do not use the development server in a production environment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
35.231.193.217 - - [02/May/2019 22:19:42] "GET /airbnb-onepage/ HTTP/1.1" 200 -
```

Window 2:

```sh
ubuntu@229-web-01:~/AirBnB_clone_v2$ curl 127.0.0.1:5000/airbnb-onepage/
Hello HBNB!ubuntu@229-web-01:~/AirBnB_clone_v2$
```

| Task                                 | File                                                     |
| ------------------------------------ | -------------------------------------------------------- |
|                                      |
| 1. Set up production with Gunicorn   | [SOON](./)                                               |
| 2. Serve a page with Nginx           | [2-app_server-nginx_config](./2-app_server-nginx_config) |
| 3. Add a route with query parameters | [3-app_server-nginx_config](./3-app_server-nginx_config) |
| 4. Let's do this for your API        | [4-app_server-nginx_config](./4-app_server-nginx_config) |
| 5. Serve your AirBnB clone           | [5-app_server-nginx_config](./5-app_server-nginx_config) |
```
