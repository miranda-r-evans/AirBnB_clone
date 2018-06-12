#!/usr/bin/env python3
''' Contains State class '''

from models.base_model import BaseModel


class State(BaseModel):
        ''' Represents a state in USA '''

        class_att_dict = {'name': str}

        def __init__(self, *args, **kwargs):
                ''' Initializes a State instance '''
                for key in State.class_att_dict.keys():
                        if key not in kwargs.keys():
                                kwargs[key] = State.class_att_dict[key]()

                super().__init__(*args, **kwargs)
