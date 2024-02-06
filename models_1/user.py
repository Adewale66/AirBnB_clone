#!/usr/bin/python3
""" Creating a new User class that inherits from BaseModel"""

from models.base_model import BaseModel


class User(BaseModel):
    """
    Defines class for User
    Attributes:
        email (string):The User's email.
        first_name (string):The User's first_name.
        last_name (string): The User's last_name.
        password (string): The User's created password.
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""
