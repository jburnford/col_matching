#!/usr/bin/env python3
"""Local dev server for the atlas with no-store caching, so edits show on plain refresh."""
import http.server, socketserver, os
os.chdir(os.path.join(os.path.dirname(__file__), "docs"))
class H(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header("Cache-Control", "no-store, no-cache, must-revalidate, max-age=0")
        self.send_header("Pragma", "no-cache")
        super().end_headers()
    def log_message(self, *a): pass
socketserver.TCPServer.allow_reuse_address = True
with socketserver.TCPServer(("0.0.0.0", 8731), H) as s:
    print("serving docs/ on :8731 (no-store)"); s.serve_forever()
