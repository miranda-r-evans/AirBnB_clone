#!/usr/bin/env python3
''' Contains Review class '''

from models.base_model import BaseModel


class Review(BaseModel):
        ''' Review of a place '''

        class_att_dict = {'place_id': str, 'user_id': str, 'text': str}

        def __init__(self, *args, **kwargs):
                ''' Initailizes Review instance with
                place_id, user_id, text (of review) '''
                for key in Review.class_att_dict.keys():
                        if key not in kwargs.keys():
                                kwargs[key] = Review.class_att_dict[key]()

                super().__init__(*args, **kwargs)
