#!/usr/bin/env python3
''' Contains Amenity class '''

from models.base_model import BaseModel


class Amenity(BaseModel):
        ''' Represents an amenity '''

        def __init__(self, *args, **kwargs):
                ''' Initializes an Amenity instance '''
                my_atts = ['name']
                for attribute in my_atts:
                        if attribute not in kwargs.keys():
                                kwargs[attribute] = ''

                super().__init__(*args, **kwargs)
