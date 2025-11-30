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