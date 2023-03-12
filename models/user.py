#!/usr/bin/python3

from models.base_model import BaseModel

class User(BaseModel):
    """subclass that inherits from Baseclass"""
    email = ''
    password = ''
    first_name = ''
    last_name = ''
    def __init__(self, *args, **kwargs):
        """constructor of user class"""
        super().__init__(self, *args, **kwargs)   
