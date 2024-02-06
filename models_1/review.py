#!/usr/bin/python3
""" This defines the Class Review"""

from models.base_model import BaseModel


class Review(BaseModel):
    """Defines class for Review

    Attributes:
        place_id (str): The id of the place.
        user_id (str): The id of the user.
        text (str): The review text by the user.
    """
    place_id = ""
    user_id = ""
    text = ""
