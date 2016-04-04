from BaseHTTPServer import HTTPServer, BaseHTTPRequestHandler
import SimpleHTTPServer
from SocketServer import ThreadingMixIn
import threading


class ThreadedHTTPServer(ThreadingMixIn, HTTPServer):
    """Handle requests in a separate thread."""
    
Handler = SimpleHTTPServer.SimpleHTTPRequestHandler
server = ThreadedHTTPServer(('localhost', 8080), Handler)
print 'Starting server, use <Ctrl-C> to stop'
server.serve_forever()
