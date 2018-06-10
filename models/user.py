#!/usr/bin/env python3
''' Contains User class '''

from models.base_model import BaseModel


class User(BaseModel):
        ''' A user of hbnb '''

        def __init__(self, *args, **kwargs):
                ''' Initializes a User Instance '''
                my_atts = ['email', 'password', 'first_name', 'last_name']
                for attribute in my_atts:
                        if attribute not in kwargs.keys():
                                kwargs[attribute] = ''
                super().__init__(*args, **kwargs)
