#!/usr/bin/env python3
''' Contains State class '''

from models.base_model import BaseModel


class State(BaseModel):
        ''' Represents a state in USA '''

        def __init__(self, *args, **kwargs):
                ''' Initializes a State instance '''
                my_atts = ['name']
                for attribute in my_atts:
                        if attribute not in kwargs.keys():
                                kwargs[attribute] = ''
                super().__init__(*args, **kwargs)
