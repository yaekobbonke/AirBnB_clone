#!/usr/bin/python3
from models.base_model import BaseModel
class City(BaseModel):
    """class that inherits from base class"""
    state_id = ''
    name = ''
    def __init__(self, *args, **kwargs):
        """a constructor of City class"""
    super().__init__(self, *args, **kwargs)
