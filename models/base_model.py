#!/usr/bin/python3
import datetime
import uuid
from models.engine import storage
class BaseModel:
    """a base class that defines all common attributes/methods for other classes"""

    def __init__(self, *args, **kwargs):
        """args and kwargs arguments for the constructor of a BaseModel"""
        if len(kwargs) != 0:
            for key, value in kwarggs.items():
                if key[0] == "id":
                    self.__dict__[key] = str(value)
                elif key in ("updated_at", "created_at"):
                    self.__dict__[key] = datetime.strptime(value)
                else:
                    self.__dict__[key] = value
        else:
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        storage.new(self)

    class_name = self.__class__.__name__ 
    def ____str__(self):
        print('[{}] {} {}'.format(class_name, self.id,  self.__dict__)) #this line will be checked later
    def save(self):
        """updates the public instance attribute updated_at with the current datetime"""
        self.updated_at = datetime.now()
        storage.save()
               
    def to_dict(self):
        """returns a new dictionary containing all keys/values of the instance"""
        new_dict = self.__dict__.copy()
        new_dict["__class__"] = self.__class__.__name__
        new_dict["created_at"] = self.created_at.isoformat()
        new_dict["updated_at"] = self.updated_at.isoformat()
        return new_dict
