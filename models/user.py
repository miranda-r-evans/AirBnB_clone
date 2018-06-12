#!/usr/bin/env python3
''' Contains User class '''

from models.base_model import BaseModel


class User(BaseModel):
        ''' A user of hbnb '''

        class_att_dict = {'email': str, 'password': str, 'first_name': str,
                          'last_name': str}

        def __init__(self, *args, **kwargs):
                ''' Initializes a User Instance '''
                for key in User.class_att_dict.keys():
                        if key not in kwargs.keys():
                                kwargs[key] = User.class_att_dict[key]()

                super().__init__(*args, **kwargs)
