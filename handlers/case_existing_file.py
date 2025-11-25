from handlers.base_case  import BaseCase
import os

class CaseExistingFile(BaseCase):


    def test(self, handler):

        path = handler.translate_path(handler.path) #returns true if the requested path is an existing file
        return os.path.isfile(path)
    
    def act(self, handler):
        handler.handle_file()#serve the file using the handler's file-serving method
    

