from http.server import HTTPServer, BaseHTTPRequestHandler
from handlers.base_case import BaseCase


class RequestHandler(BaseHTTPRequestHandler):
    """Handle HTTP requests."""
    
    def send_content(self, content, status=200):
        """Send content to the client."""
        self.send_response(status)
        self.send_header("Content-type", "text/html")
        self.send_header("Content-Length", str(len(content)))
        self.end_headers()
        self.wfile.write(content)
    
    def handle_error(self, msg):
        """Send a 404 error message."""
        content = f"Error: {msg}".encode('utf-8')
        self.send_content(content, 404)
    
    def do_GET(self):
        """Handle GET requests."""
        message = "<h1>Server is running. BaseCase setup complete.</h1>"
        self.send_content(message.encode('utf-8'))


def main():
    """Run the server."""
    server_address = ('', 8080)
    httpd = HTTPServer(server_address, RequestHandler)
    
    print("Server running on http://localhost:8080")
    print("Press Ctrl+C to stop the server")
    
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nShutting down server...")
        httpd.shutdown()


if __name__ == '__main__':
    main()