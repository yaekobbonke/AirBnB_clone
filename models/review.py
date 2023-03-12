#!/usr/bin/python3
from model.base_model import BaseModel
class Review(BaseModel):
    """review class that inherits from base class"""

    place_id = ''
    user_id = ''
    text = ''

    def __init__(self, *args, **kwargs):
        """a constructor that initializes Review class"""
    super().__init__(self, *args, *kwargs)
