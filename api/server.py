import os
from http.server import SimpleHTTPRequestHandler, HTTPServer
import json

# Retrieve the flag from the environment variable, fallback to a default value
SECRET_FLAG = os.getenv("SECRET_FLAG", "No flag found")

class FlagHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/flag":
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps({"flag": SECRET_FLAG}).encode())
        else:
            self.send_response(404)
            self.end_headers()

if __name__ == "__main__":
    server_address = ("", 5000)  # Listen on port 5000
    httpd = HTTPServer(server_address, FlagHandler)
    print("Serving on port 5000...")
    httpd.serve_forever()
