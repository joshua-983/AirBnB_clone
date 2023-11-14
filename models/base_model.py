#!/usr/bin/python3
""" AirBnB BaseModel"""
from uuid import uuid4
from datetime import datetime
import models


class BaseModel:
    """ Definition of the BaseModel """

    def __init__(self, *args, **kwargs):
        """ Initializes a new instance of BaseModel
        """
        if kwargs is None or len(kwargs) == 0:
            self.id = str(uuid4())
            self.created_at = datetime.today()
            self.updated_at = datetime.today()
            models.storage.new(self)
        else:
            for key, value in kwargs.items():
                if key in ["created_at", "updated_at"]:
                    self.__dict__[key] = datetime\
                            .strptime(value, "%Y-%m-%dT%H:%M:%S.%f")

                elif key == "id":
                    self.id = value
                elif key == "__class__":
                    self.__class__.__name__ = kwargs[key]
                else:
                    setattr(self, key, value)

    def save(self):
        """ updates the instance attribute update_at with current datetime"""
        self.update_at = datetime.today()
        models.storage.save()

    def to_dict(self):
        """returns a dictionary containing all keys/values of __dict__
        of the instance

        Includes the key/value pair __class__ representing the class name
        of the object."""
        instance_dict = self.__dict__.copy()
        instance_dict["created_at"] = self.created_at.isoformat()
        instance_dict["updated_at"] = self.updated_at.isoformat()
        instance_dict["__class__"] = self.__class__.__name__
        return instance_dict

    def __str__(self):
        """ String representation of BaseModel instances"""
        classname = self.__class__.__name__
        return "[<{}>] (<{}>) <{}>".format(classname, self.id, self.__dict__)
