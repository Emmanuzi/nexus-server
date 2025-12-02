import os
from handlers.base_case import BaseCase


class CaseDirectoryIndexFile(BaseCase):
    """
    Serves index.html when a directory request contains one.
        
    If a user requests a directory (e.g., /pages/) and that directory 
    does not contain an 'index.html', this handler will serve 
    'index.html' from the parent directory.
    """
    
    def test(self, handler):
        """
        Checks if the request path is a directory AND contains index.html.
        """
        # 1. Is the requested path a directory?
        is_dir = os.path.isdir(handler.full_path)
        
        # 2. Does index.html exist inside it? 
        # (We use the helper method index_path() from BaseCase)
        has_index = os.path.isfile(self.index_path(handler))
        
        return is_dir and has_index

    def act(self, handler):
        """
        Serves the index.html file.
        """
        # Calculate the path to index.html
        full_path = self.index_path(handler)
        
        # Use the helper method from BaseCase to send the file
        self.handle_file(handler, full_path)


class CaseDirectoryNoIndexFile(BaseCase):
    def test(self, handler):
        is_dir = os.path.isdir(handler.full_path)
        has_no_index = not os.path.isfile(self.index_path(handler))
        return is_dir and has_no_index

    def act(self, handler):
        return handler.list_dir()      

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
