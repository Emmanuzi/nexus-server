
import os
from http.server import HTTPServer, BaseHTTPRequestHandler 
from handlers.case_no_file import CaseNoFile
from handlers.case_existing_file import CaseExistingFile
from handlers.case_directory import CaseDirectory

Cases = [
    CaseNoFile(),
    CaseExistingFile(),
    CaseDirectory(),
]

class MyHandler(BaseHTTPRequestHandler):

    def path_exists(self):
        path = self.translate_path(self.path)
        return os.path.exists(path)

    def do_GET(self):
        # Try each case in order
        for case in Cases:
            if case.test(self):
                return case.act(self)

        # fallback
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(b"Server is running!")

    def handle_file(self):
        path = self.translate_path(self.path)

        try:
            with open(path, "rb") as file:
                self.send_response(200)
                self.end_headers()
                self.wfile.write(file.read())
        except FileNotFoundError:
            self.send_error(404, "File not found")


PORT = 8000
os.chdir("www")
server = HTTPServer(("localhost", PORT), MyHandler)
print(f"Server running at http://localhost:{PORT}")
server.serve_forever()

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


