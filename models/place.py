#!/usr/bin/env python3
''' Contains Place class '''

from models.base_model import BaseModel


class Place(BaseModel):
        ''' A place for rent, in a location and with serveral features '''

        class_att_dict = {'city_id': str, 'user_id': str, 'name': str,
                          'description': str, 'number_rooms': int,
                          'number_bathrooms': int, 'max_guest': int,
                          'price_by_night': int, 'latitude': float,
                          'longitude': float, 'amenity_id': list}

        city_id = ''
        user_id = ''
        name = ''
        description = ''
        number_rooms = 0
        number_bathrooms = 0
        max_guest = 0
        price_by_night = 0
        latitude = 0.0
        longitude = 0.0
        amenity_id = []