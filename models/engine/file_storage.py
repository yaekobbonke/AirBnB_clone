#!/usr/bin/python3

import json

class FileStorage:
    """a class that serializes instances to a JSON file and deserializes JSON file to instances"""

    __file_path = open('file.json')
    __objects = {}

    def all(self):
        """returns a dictionary __objects"""
        return __objects
    def new(self, obj):
        <obj class name>.id = obj
    def save(self):
        json.dump(__objects)
    def reload(self):
        if __file_path True:
            json.load(__objects)
        else:
            return 0



