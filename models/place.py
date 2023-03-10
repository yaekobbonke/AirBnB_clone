#!/usr/bin/python3

class Place(BaseModel):
    """class that inherits from base class"""
    city_id = ''
    user_id = ''
    name = ''
    description = ''
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = ''

    super().__init__(self, *args, **kwargs):
