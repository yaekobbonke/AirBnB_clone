#!/usr/bin/python3

class City(BaseModel):
    """class that inherits from base class"""
    state_id = ''
    name = ''

    super().__init__(self, *args, **kwargs):
