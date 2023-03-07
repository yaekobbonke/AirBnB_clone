#!/usr/bin/python3
import datetime
import uuid

class BaseModel:
    """a base class that defines all common attributes/methods for other classes"""
   
   def __init__(self, id, created_at, updated_at):
       """a constructor that initializes Public instance attributes"""
       self.id = uuid.uuid4()
       self.created_at = datetime.now()
       self.updated_at = datetime.now()
    def ____str__(self):
        print('{} {} {}'.format(BaseModel, self.id, self, self.__dict__)) #this line will be checked later
    def save(self):
        return self.updated_at
    def to_dict(self):
        return json.dump(self.created_at) #will be checked and  updated
