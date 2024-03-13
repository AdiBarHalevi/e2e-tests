from .base import BaseModel


class Error(BaseModel):
    def __init__(self, message: str, code: int, **kwargs):
        """
        Initialize Error
        Parameters:
        ----------
            message: str
            code: int
        """
        self.message = message
        self.code = code
