#!/usr/bin/env python

from wsgiref.simple_server import make_server
import socket


def get_hostname(environ, start_response):
  if hasattr(socket, 'setdefaulttimeout'):
    socket.setdefaulttimeout(5) # Seconds
  hostname = socket.gethostbyaddr(environ['REMOTE_ADDR'])
  status = '200 OK'
  response_headers = [('Content-type','text/plain')]
  start_response(status, response_headers)
  return hostname[0]


if __name__ == '__main__':
  httpd = make_server('', 8000, get_hostname)
  print "Serving HTTP on port 8000..."
  httpd.serve_forever()

