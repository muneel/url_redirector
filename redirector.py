"""
URL Redirection

Summary:
Sends the HTTP header response based on the code received.
Converts the URL received into Location in the response.

Example:
$ curl -i http://127.0.0.1:5000/301/http://www.google.com
HTTP/1.0 301 Moved Permanently
Server: BaseHTTP/0.3 Python/2.7.5
Date: Wed, 19 Apr 2017 20:06:11 GMT
Location: http://www.google.com

$ curl -i http://127.0.0.1:5000/302/http://www.google.com
HTTP/1.0 302 Found
Server: BaseHTTP/0.3 Python/2.7.5
Date: Wed, 19 Apr 2017 20:06:17 GMT
Location: http://www.google.com

$ curl -i http://127.0.0.1:5000/303/http://www.google.com
HTTP/1.0 303 See Other
Server: BaseHTTP/0.3 Python/2.7.5
Date: Wed, 19 Apr 2017 20:06:22 GMT
Location: http://www.google.com
"""

import BaseHTTPServer
import time
import sys

HOST_NAME = ''
PORT_NUMBER = 5000


class RedirectHandler(BaseHTTPServer.BaseHTTPRequestHandler):
    def do_HEAD(s):
        """Sends only headers when HEAD is requested

        Args:
            None:

        Returns:
            None
        """
        s.end_headers()

    def do_GET(s):
        """GET request from getting URL Redirection with return status code

        Args:
            None

        Returns:
            None

        """
        print s.path
        try:
            temp = str(s.path)
            code = int(temp[1:4])
            url = temp[5:]
            if code in (301, 302, 303, 307):
                s.__send_redirect(code, url)
            else:
                s.send_response(400)
                s.end_headers()
        except:
            s.send_response(400)
            s.end_headers()

    def __send_redirect(s, code, url):
        s.send_response(code)
        s.send_header("Location", url)
        s.end_headers()


if __name__ == '__main__':
    if len(sys.argv) == 2:
        PORT_NUMBER = int(sys.argv[1])
    server_class = BaseHTTPServer.HTTPServer
    httpd = server_class((HOST_NAME, PORT_NUMBER), RedirectHandler)
    print time.asctime(), "Server Starts - %s:%s" % (HOST_NAME, PORT_NUMBER)
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()
    print time.asctime(), "Server Stops - %s:%s" % (HOST_NAME, PORT_NUMBER)
