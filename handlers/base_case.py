import os

class BaseCase:
    """Base class for request handlers."""

    def handle_file(self, handler, full_path):
        """Read and send a file."""
        try:
            with open(full_path, 'rb') as reader:
                content = reader.read()
            handler.send_response(200)
            handler.end_headers()
            handler.wfile.write(content)
        except IOError as msg:
            handler.send_error(404, f"Cannot read file: {msg}")

    def index_path(self, handler):
        """Return the full path to index.html inside the directory."""
        return os.path.join(handler.full_path, 'index.html')

    def test(self, handler):
        raise NotImplementedError()

    def act(self, handler):
        raise NotImplementedError()

