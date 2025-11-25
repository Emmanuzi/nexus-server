from handlers.base_case import BaseCase

class CaseNoFile(BaseCase):
    def test(self, handler):
        # This case is true when the requested path does NOT exist
        return not handler.path_exists()

    def act(self, handler):
        # Handle the situation when the file does not exist
        handler.handle_error(404, f"File not found: {handler.full_path}")