#!/usr/bin/python3

from models.base_model import BaseModel
from models.user import User
import json

class FileStorage:
    """a class that serializes instances to a JSON file and deserializes JSON file to instances"""

    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """returns a dictionary __objects"""
        return self. __objects
    def new(self, object):
        """sets in __objects the object with the key <obj class name>.id"""
        self.__objects[object.__class__.__name__ + '.' + str(object)] = object
    def save(self):
        """serializes __objects to the JSON file"""
        with open(self.__file_path.json, "w") as f:
            json.dump({k: v.to_dict() for k, v in self.__objects.items()}, f)
    def reload(self):
        """deserializes the JSON file to __objects (only if the JSON file (__file_path) exists ; otherwise, do nothing)"""
        try:
            with open(self.__file_path, 'r') as f:
                dict = json.loads(f.read())
                for value in dict.values():
                    cls = value["__class__"]
                    self.new(eval(cls)(**value))
        except Exception:
            pass
