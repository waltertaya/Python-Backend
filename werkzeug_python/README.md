# Werkzeug Tutorial

- It is comprehensive WSGI(Web Server Gateway Interface) web application library for Python.
- WSGI is a specification that defines a standard interface between web servers and Python web applications or frameworks.
- WSGI serves as a common protocol for communication between web servers and python applications, ensuring that they work together seamlessly regardless of the specific web server or application framework being used.

### Key Features of WSGI

1. `Standardization: ` It provides a standardized way for web servers to interact with Python applications. This allows developers to use web servers(like Apache, Nginx, or Gunicorn) with their Python applications without requiring changes to the application code.
2. `Decoupling: ` By defining a clear interface, WSGI decouples(to eliminate the interrelationship of) the web server from the web application. This means developers can choose different components for their stack, such as different web servers or middleware, without worrying about the compatability issues.
3. `Middleware Support: ` WsGI allows for the use of the middleware, which are components that sit down between the server and the application. Middleware can modify the request and response, handle authentication, logging, session, management, etc.

### How WSGI Works

- WSGI defines a callable object (typically a function) that takes two arguments: environ and start_response.

    1. environ: A dictionary containing the CGI-style environment variables, which include information about the request, such as headers, the request method, query string, and more.

    2. start_response: A callback function that the application must call to start the HTTP response. It takes the status code, response headers, and an optional exception.

- The WSGI application, once called, returns an iterable that produces the response body.

## Author

- [waltertaya](https://www.github.com/waltertaya)
