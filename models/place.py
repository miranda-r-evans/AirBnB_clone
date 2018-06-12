#!/usr/bin/env python3
''' Contains Place class '''

from models.base_model import BaseModel


class Place(BaseModel):
        ''' A place for rent, in a location and with serveral features '''

        class_att_dict = {'city_id': str, 'state_id': str, 'name': str,
                          'description': str, 'number_rooms': int,
                          'number_bathrooms': int, 'max_guest': int,
                          'price_by_night': float, 'latitude': float,
                          'longitude': float}

        def __init__(self, *args, **kwargs):
                ''' Initializes a Place instace '''
                for key in Place.class_att_dict.keys():
                        if key not in kwargs.keys():
                                kwargs[key] = Place.class_att_dict[key]()

                super().__init__(*args, **kwargs)
