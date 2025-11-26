import os

class BaseCase:
    """Base class for request handlers."""
    
    def handle_file(self, handler, full_path):
        """Read and send a file to the client."""
        try:
            with open(full_path, 'rb') as reader:
                content = reader.read()
            handler.send_content(content)
        except IOError as msg:
            error_msg = "'{0}' cannot be read: {1}".format(full_path, msg)
            handler.handle_error(error_msg)
    
    def index_path(self, handler):
        """Return the path to index.html in the given directory."""
        return os.path.join(handler.full_path, 'index.html')
    
    def test(self, handler):
        """Determine if this handler can process the request."""
        raise NotImplementedError
    
    def act(self, handler):
        """Execute the handler's action."""
        raise NotImplementedError