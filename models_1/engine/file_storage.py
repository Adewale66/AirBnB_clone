#!/usr/bin/python
""" Module to create a persistent file storage system"""


import datetime
import json
import uuid


class FileStorage:
    """
    a class that serializes instances to a JSON file and
    deserializes JSON files to instances
    """
    __file_path = 'file.json'
    __objects = {}

    """ Public instance methods"""
    def all(self):
        """ returns the dictionary rep of __objects"""
        return self.__class__.__objects

    def new(self, obj):
        """ method to set __objects"""
        key = '{}.{}'.format(obj.__class__.__name__, obj.id)
        self.__class__.__objects[key] = obj
        """ confirm the key/value assignment"""

    def save(self):
        """ save a file to a Json Object"""
        new_objects = {}
        for key, value in self.__class__.__objects.items():
            new_objects[key] = value.to_dict()
        with open(self.__file_path, 'w') as file:
            json.dump(new_objects, file, default=str)

    """ refactror this entire reload method using another logic"""
    def reload(self):
        """ deserializes a json file to __objects"""
        try:
            with open(self.__class__.__file_path, "r") as file:
                data = json.load(file)
                for key, value in data.items():
                    class_name, obj_id = key.split('.')
                    """ import Base Model here """
                    from models.base_model import BaseModel
                    from models.amenity import Amenity
                    from models.city import City
                    from models.place import Place
                    from models.review import Review
                    from models.state import State
                    from models.user import User
                    """imports done"""
                    obj_instance = eval(class_name)(**value)
                    self.__class__.__objects[key] = obj_instance
            return self.__class__.__objects
        except (FileNotFoundError, IOError):
            return {}
