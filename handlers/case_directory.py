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
        pass  # Logic coming in next commit

    def act(self, handler):
        pass  # Logic coming in next commit