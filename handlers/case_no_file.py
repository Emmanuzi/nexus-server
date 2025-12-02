import os
from handlers.base_case import BaseCase

class CaseNoFile(BaseCase):
    """Handles requests for paths that do not exist."""

    def test(self, handler):
        """Return True if the requested path does not exist."""
        full_path = handler.translate_path(handler.path)
        return not os.path.exists(full_path)

    def act(self, handler):
        """Send a 404 error response."""
        full_path = handler.translate_path(handler.path)
        handler.send_response(404)
        handler.send_header("Content-type", "text/html")
        handler.end_headers()
        handler.wfile.write(f"File not found: {full_path}".encode('utf-8'))
