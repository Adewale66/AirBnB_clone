#!/usr/bin/python3
""" Module for FileStorage class """


import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
    """ FileStorage class """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ Returns the dictionary __objects """
        return FileStorage.__objects

    def new(self, obj):
        """ Sets in __objects the obj with key <obj class name>.id """

        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """ Serializes __objects to the JSON file (path: __file_path) """

        with open(FileStorage.__file_path, "w") as file:
            json.dump(
                {k: o.to_dict() for k, o in FileStorage.__objects.items()},
                file
                )

    def reload(self):
        """ Deserializes the JSON file to __objects """
        try:
            with open(FileStorage.__file_path, "r") as file:
                obj_dict = json.load(file)
                for _, value in obj_dict.items():
                    cls_name = value["__class__"]
                    del value["__class__"]
                    cls = eval(cls_name)
                    self.new(cls(**value))
        except FileNotFoundError:
            return
