#!/usr/bin/python3
"""Definition for City class"""
from models.base_model import BaseModel


class City(BaseModel):
    """Class definition
    Attributes:
        state_id(str): the state of City
        name(str): the city name
    """

    state_id = ""
    name = ""
