#!/usr/bin/python3
import datetime
import uuid
from models.__init__ import storage

class BaseModel:
    """a base class that defines all common attributes/methods for other classes"""
   
   def __init__(self, id, created_at, updated_at):
       """a constructor that initializes Public instance attributes"""
       self.id = uuid.uuid4()
       self.created_at = datetime.now()
       self.updated_at = datetime.now()

    def ____init__(self, *args, **kwargs):  #will be checked
        

    def ____str__(self):
        print('{} {} {}'.format(BaseModel, self.id, self, self.__dict__)) #this line will be checked later
    def save(self):
        return self.updated_at
        storage.save()
    def to_dict(self):
        return json.dump(self.created_at) #will be checked and  updated
