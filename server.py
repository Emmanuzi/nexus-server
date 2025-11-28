
from http.server import HTTPServer, SimpleHTTPRequestHandler 
from handlers.case_no_file import CaseNoFile
from handlers.case_existing_file import CaseExistingFile
from handlers.case_directory import CaseDirectory
import os
import urllib

Cases = [
    CaseNoFile(),
    CaseExistingFile(),
    CaseDirectory(),
]

class MyHandler(SimpleHTTPRequestHandler):
    
    def translate_path(self, path):
        """Map URL path to filesystem path under 'www' folder."""
        path = urllib.parse.unquote(path)
        # Use 'www' as root folder
        full_path = os.path.join(os.getcwd(), "www", path.lstrip("/"))
        return full_path





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

    


PORT = 8000
server = HTTPServer(("localhost", PORT), MyHandler)
print(f"Server running at http://localhost:{PORT}")
server.serve_forever()


