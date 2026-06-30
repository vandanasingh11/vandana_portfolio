from http.server import ThreadingHTTPServer, SimpleHTTPRequestHandler
import sys

class MyHandler(SimpleHTTPRequestHandler):
    def end_headers(self):
        # Enable CORS and Disable caching for development
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Cache-Control', 'no-store, no-cache, must-revalidate, max-age=0')
        super().end_headers()

def run(port=8000):
    server_address = ('', port)
    httpd = ThreadingHTTPServer(server_address, MyHandler)
    print(f"Starting multi-threaded HTTP server on port {port}...")
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nKeyboard interrupt received, exiting.")
        sys.exit(0)

if __name__ == '__main__':
    port = 8000
    if len(sys.argv) > 1:
        port = int(sys.argv[1])
    run(port)
