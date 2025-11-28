import os
from handlers.base_case  import BaseCase


class CaseExistingFile(BaseCase):


    def test(self, handler):
        """Return True if the requested path is a file."""
        full_path = handler.translate_path(handler.path)
        return os.path.isfile(full_path)

    def act(self, handler):
        """Serve the file using BaseCase's handle_file method."""
        full_path = handler.translate_path(handler.path)
        return self.handle_file(handler, full_path)
    

