#!/usr/bin/env python3

import http.server as SimpleHTTPServer
import socketserver as SocketServer
import optparse
from functools import partial

PORT = 3737

class GetHandler(SimpleHTTPServer.SimpleHTTPRequestHandler):
    def __init__(self, person, *args, **kwargs):
        self.person = person
        # BaseHTTPRequestHandler calls do_GET **inside** __init__ !!!
        # So we have to call super().__init__ after setting attributes.
        super().__init__(*args, **kwargs)

    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(str.encode(f'Hello, {options.person}!'))

# Parse options.
p = optparse.OptionParser()
p.add_option('--person', '-p', default="world")
options, arguments = p.parse_args()

# Initialize handler
Handler = partial(GetHandler, options.person)
httpd = SocketServer.TCPServer(("", PORT), Handler)

# Listen
httpd.serve_forever()
