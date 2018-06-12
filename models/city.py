#!/usr/bin/env python3
''' Contains City class '''

from models.base_model import BaseModel


class City(BaseModel):
        ''' Represents a city '''

        class_att_dict = {'name': str, 'state_id': str}

        def __init__(self, *args, **kwargs):
                ''' Initializes a City instance with a name and state id '''
                for key in City.class_att_dict.keys():
                        if key not in kwargs.keys():
                                kwargs[key] = City.class_att_dict[key]()

                super().__init__(*args, **kwargs)
