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


