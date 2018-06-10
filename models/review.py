#!/usr/bin/env python3
''' Contains Review class '''

from models.base_model import BaseModel


class Review(BaseModel):
        ''' Review of a place '''

        def __init__(self, *args, **kwargs):
                ''' Initailizes Review instance with
                place_id, user_id, text (of review) '''
                my_atts = ['place_id', 'user_id', 'text']
                for attribute in my_atts:
                        if attribute not in kwargs.keys():
                                kwargs[attribute] = ''
                if 'amenity_id' not in kwargs:
                        kwargs['amenity_id'] = []

                super().__init__(*args, **kwargs)
