#!/usr/bin/python3

""" Module to handle console input/output"""


import cmd
import re
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models import storage


class HBNBCommand(cmd.Cmd):
    """ Class to handle console input/output """
    prompt = '(hbnb) '
    model_names = [
        "BaseModel", "User", "State", "City", "Amenity", "Place", "Review"
        ]

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program"""
        return True

    def emptyline(self):
        """Do nothing for an emptyline"""
        pass

    def do_create(self, arg):
        """Creates a new instance of BaseModel, saves it to JSON file"""
        if arg == "":
            print("** class name missing **")
            return
        if arg not in self.model_names:
            print("** class doesn't exist **")
            return
        obj = eval(arg)()
        obj.save()
        print(obj.id)

    def do_show(self, arg):
        """Prints the string representation of an instance based on class"""
        if self.check_error(arg):
            return
        id = arg.split()[1]
        for _, value in storage.all().items():
            if value.id == id and value.__class__.__name__ == arg.split()[0]:
                print(value)
                return
        print("** no instance found **")

    def do_destroy(self, arg):
        """ Deletes an instance based on the class name and id"""
        if self.check_error(arg):
            return
        id = arg.split()[1]
        for key, value in storage.all().items():
            if value.id == id and value.__class__.__name__ == arg.split()[0]:
                del storage.all()[key]
                storage.save()
                return
        print("** no instance found **")

    def check_error(self, arg):
        """Helper function to check for class and id"""
        model, id = arg.split() + [""] * (2 - len(arg.split()))
        if model == "":
            print("** class name missing **")
            return True
        if model not in self.model_names:
            print("** class doesn't exist **")
            return True
        if id == "":
            print("** instance id missing **")
            return True
        return False

    def do_all(self, arg):
        """ Prints all string representation of all instances"""
        value_list = []
        if arg == "":
            for value in storage.all().values():
                value_list.append(str(value))
            print(value_list)
            return
        if arg not in self.model_names:
            print("** class doesn't exist **")
            return
        for value in storage.all().values():
            if value.__class__.__name__ == arg:
                value_list.append(str(value))
        print(value_list)

    def do_update(self, arg):
        """ Updates an instance based on the class name and id"""
        items = []
        for i in arg.split():
            items.append(i)
        model = items[0] if len(items) > 0 else ""
        id = items[1] if len(items) > 1 else ""
        attr = items[2] if len(items) > 2 else ""
        value = items[3] if len(items) > 3 else ""

        if model == "":
            print("** class name missing **")
            return
        if model not in self.model_names:
            print("** class doesn't exist **")
            return
        if id == "":
            print("** instance id missing **")
            return
        if attr == "":
            print("** attribute name missing **")
            return
        if value == "":
            print("** value missing **")
            return

        for _, obj in storage.all().items():
            if obj.id == id and obj.__class__.__name__ == model:
                if hasattr(obj, attr):
                    value = type(getattr(obj, attr))(value)
                setattr(obj, attr, value)
                storage.save()
                return
        print("** no instance found **")

    def default(self, arg):
        """Called on an input line when the command prefix is not recognized"""
        args = arg.split(".")
        if len(args) < 2:
            print("*** Unknown syntax: {}".format(arg))
            return
        model = args[0]
        if model not in self.model_names:
            print("** class doesn't exist **")
            return
        if args[1] == "all()":
            self.do_all(model)
        elif args[1] == "count()":
            count = 0
            for value in storage.all().values():
                if value.__class__.__name__ == model:
                    count += 1
            print(count)
        elif args[1].startswith("show("):
            id = args[1][6:-2]
            self.do_show(model + " " + id)
        elif args[1].startswith("destroy("):
            id = args[1][9:-2]
            self.do_destroy(model + " " + id)
        elif args[1].startswith("update("):
            if "{" in args[1]:
                args = re.split(r'[\(\),]', args[1])
                id = args[1][1:-1]
                kwargs = args[2:-1]
                for obj in kwargs:
                    attr, value = obj.split(":")
                    if "{" in attr:
                        attr = attr.strip()[2:-1]
                    else:
                        attr = attr.strip()[1:-1]
                    if "}" in value and "\"" in value:
                        value = value.strip()[1:-2]
                    elif "\"" in value:
                        value = value.strip()[1:-1]
                    elif "}" in value and "\"" not in value:
                        value = value.strip()[:-1]
                    self.do_update(model + " " + id + " " + attr + " " + value)
            else:
                args = re.split(r'[\(\),]', args[1])
                id = args[1][1:-1]
                attr = args[2].strip()[1:-1]
                value = args[3].strip()[1:-1]
                self.do_update(model + " " + id + " " + attr + " " + value)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
