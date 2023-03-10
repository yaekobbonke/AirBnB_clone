#!/usr/bin/python3

class Review(BaseModel):
    """review class that inherit from base class"""

    place_id = ''
    user_id = ''
    text = ''

    super().__init__(self, *args, *kwargs):
