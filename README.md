# url_redirector
URL Redirection with different codes
'''
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


'''
