class BaseCase:
    """Base class for request handlers."""
    
    def test(self, handler):
        """Determine if this handler can process the request."""
        raise NotImplementedError
    
    def act(self, handler):
        """Execute the handler's action."""
        raise NotImplementedError