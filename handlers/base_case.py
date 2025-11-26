class BaseCase:
    def test(self, handler):
        """Return True if this case should handle the request."""
        raise NotImplementedError()

    def act(self, handler):
        """Perform the action for this case."""
        raise NotImplementedError()
