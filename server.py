import os
from http.server import HTTPServer, BaseHTTPRequestHandler
from handlers.case_directory import CaseDirectoryIndexFile

class RequestHandler(BaseHTTPRequestHandler):
    """Main HTTP request handler for the server."""
    
    def send_content(self, content, status=200):
        """Sends HTTP response with content to the client."""
        self.send_response(status)
        self.send_header("Content-type", "text/html")
        self.send_header("Content-Length", str(len(content)))
        self.end_headers()
        self.wfile.write(content)
    
    def handle_error(self, msg):
        """Sends a 404 error message."""
        content = f"Error: {msg}".encode('utf-8')
        self.send_content(content, 404)
    
    def do_GET(self):
        """Handle GET requests."""
        # Calculate absolute path to requested file
        self.full_path = os.getcwd() + self.path
        
        # Try to handle directory index request
        case = CaseDirectoryIndexFile()
        if case.test(self):
            case.act(self)
        else:
            # Fallback when no index.html found
            msg = "Not Found:Directory does not contain an index.html file"
            self.handle_error(msg)


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