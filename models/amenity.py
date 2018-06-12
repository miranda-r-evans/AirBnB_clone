#!/usr/bin/env python3
''' Contains Amenity class '''

from models.base_model import BaseModel


class Amenity(BaseModel):
        ''' Represents an amenity '''

        class_att_dict = {'name': str}

        def __init__(self, *args, **kwargs):
                ''' Initializes an Amenity instance '''
                for key in Amenity.class_att_dict.keys():
                        if key not in kwargs.keys():
                                kwargs[key] = Amenity.class_att_dict[key]()

                super().__init__(*args, **kwargs)
