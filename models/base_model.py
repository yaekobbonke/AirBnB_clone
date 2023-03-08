#!/usr/bin/python3
import datetime
import uuid

class BaseModel:
    """a base class that defines all common attributes/methods for other classes"""

    def __init__(self, id, created_at, updated_at):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    class_name = self.__class__.__name__ 
    def ____str__(self):
        print('{} {} {}'.format(class_name, self.id,  self.__dict__)) #this line will be checked later
    def save(self):
        """updates the public instance attribute updated_at with the current datetime"""
        self.updated_at = datetime.now()
               
    def to_dict(self):
        """returns a dictionary containing all keys/values of the instance"""
        created_at.isoformat()
        updated_at.isoformat()
        return self.__dict__
