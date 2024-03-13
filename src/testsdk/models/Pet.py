from .base import BaseModel


class Pet(BaseModel):
    def __init__(self, name: str, id: int, tag: str = None, **kwargs):
        """
        Initialize Pet
        Parameters:
        ----------
            name: str
            id: int
            tag: str
        """
        self.name = name
        self.id = id
        if tag is not None:
            self.tag = tag
