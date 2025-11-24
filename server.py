from http.server import HTTPServer, BaseHTTPRequestHandler

class RequestHandler(BaseHTTPRequestHandler):
    """Handle HTTP requests."""
    
    def do_GET(self):
        """Handle GET requests."""
        # Basic implementation - will be extended with case handlers later
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        
        message = "<h1>Hello! The server is working!</h1>"
        self.wfile.write(message.encode('utf-8'))


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

