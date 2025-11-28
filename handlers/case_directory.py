import os
from handlers.base_case import BaseCase

class CaseDirectory(BaseCase):
    """Serve a directory if the requested path is a folder."""

    def test(self, handler):
        """Return True if the requested path is a directory."""
        full_path = handler.translate_path(handler.path)
        return os.path.isdir(full_path)

    def act(self, handler):
        """Serve index.html inside the directory using BaseCase helper."""
        full_path = handler.translate_path(handler.path)
        index_file = os.path.join(full_path, "index.html")
        return self.handle_file(handler, index_file)
