#!/usr/bin/env python3
''' Contains Place class '''

from models.base_model import BaseModel


class Place(BaseModel):
        ''' A place for rent, in a location and with serveral features '''

        def __init__(self, *args, **kwargs):
                ''' Initializes a Place instace '''
                my_atts = ['city_id', 'state_id', 'name', 'description']
                my_ints = ['number_rooms', 'number_bathrooms', 'max_guest']
                my_floats = ['price_by_night', 'latitude', 'longitude']
                for attribute in my_atts:
                        if attribute not in kwargs.keys():
                                kwargs[attribute] = ''
                for attribute in my_ints:
                        if attribute not in kwargs.keys():
                                kwargs[attribute] = 0
                for attribute in my_floats:
                        if attribute not in kwargs.keys():
                                kwargs[attribute] = 0.0
                if 'amenity_id' not in kwargs:
                        kwargs['amenity_id'] = []

                super().__init__(*args, **kwargs)
