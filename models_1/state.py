#!/usr/bin/python3
""" This defines a State Class"""

from models.base_model import BaseModel


class State(BaseModel):
    """Defines class for State

    Attributes:
        name (str): The name of the state.
    """

    name = ""
