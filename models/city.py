#!/usr/bin/env python3
''' Contains City class '''

from models.base_model import BaseModel


class City(BaseModel):
        ''' Represents a city '''

        def __init__(self, *args, **kwargs):
                ''' Initializes a City instance with a name and state id '''
                my_atts = ['name', 'state_id']
                for attribute in my_atts:
                        if attribute not in kwargs.keys():
                                kwargs[attribute] = ''
                super().__init__(*args, **kwargs)
