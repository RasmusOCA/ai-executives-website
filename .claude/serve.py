import os, sys
from http.server import HTTPServer, SimpleHTTPRequestHandler

port = int(os.environ.get("PORT", 8080))
os.chdir("/Users/rasmusherning/Documents/ai-executives-website")
HTTPServer(("", port), SimpleHTTPRequestHandler).serve_forever()
