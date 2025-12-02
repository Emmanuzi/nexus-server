
from http.server import HTTPServer, SimpleHTTPRequestHandler 
from handlers.case_no_file import CaseNoFile
from handlers.case_existing_file import CaseExistingFile
from handlers.case_directory import CaseDirectory, CaseDirectoryNoIndexFile, CaseDirectoryIndexFile
import os
import urllib

Cases = [
    CaseNoFile(),
    CaseExistingFile(),
    CaseDirectoryIndexFile(),
    CaseDirectoryNoIndexFile(),
    CaseDirectory(),
]

class MyHandler(SimpleHTTPRequestHandler):
    
    def translate_path(self, path):
        """Map URL path to filesystem path under 'www' folder."""
        path = urllib.parse.unquote(path)
        # Use 'www' as root folder
        full_path = os.path.join(os.getcwd(), "www", path.lstrip("/"))
        return full_path
    


    def send_content(self, content, status=200):
        """Send HTTP response with content and status."""
        self.send_response(status)
        self.send_header("Content-type", "text/html")
        self.send_header("Content-Length", str(len(content)))
        self.end_headers()
        self.wfile.write(content)





    def list_dir(self):
        """Return a simple HTML listing of the directory contents."""
        try:
            path = self.full_path  # full_path should be set in do_GET
            entries = os.listdir(path)
            entries.sort()
            
            # Build a simple HTML page
            content = "<html><body><h2>Directory listing</h2><ul>"
            for entry in entries:
                # Make directories appear with trailing slash
                display_name = entry
                full_entry_path = os.path.join(path, entry)
                if os.path.isdir(full_entry_path):
                    display_name += "/"
                content += f'<li><a href="{entry}">{display_name}</a></li>'
            content += "</ul></body></html>"
            
            # Send response
            self.send_content(content.encode("utf-8"), 200)
        except Exception as e:
            self.send_content(f"Error listing directory: {e}".encode("utf-8"), 500)

    def do_GET(self):
        self.full_path = self.translate_path(self.path)
        # Try each case in order
        for case in Cases:
            if case.test(self):
                return case.act(self)

        # fallback
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.send_content(b"Server is running!")





    


PORT = 8000
server = HTTPServer(("localhost", PORT), MyHandler)
print(f"Server running at http://localhost:{PORT}")
server.serve_forever()


