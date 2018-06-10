#!/usr/bin/env python3
''' unit testing for file storage class '''

import unittest
import json
import models
from import_classes import *


class TestFileStorage(unittest.TestCase):
        ''' class for testing File Storage '''

        def test_store_object(self):
                ''' testing storage of objects '''
                test_dict = {'id': 'testing_storage',
                             'created_at': '2018-06-08T19:45:36.469639',
                             'updated_at': '2018-06-08T19:45:36.469672',
                             'test_attribute': 'still_arbitrary'}
                a = BaseModel(**test_dict)
                b = Place(**test_dict)
                with open('file.json', 'r') as f:
                        file_dict = json.load(f)

                self.assertTrue('BaseModel.testing_storage' in file_dict.keys())
                self.assertEqual(a.to_dict(), file_dict['BaseModel.testing_storage'])

                self.assertTrue('Place.testing_storage' in file_dict.keys())
                self.assertEqual(b.to_dict(), file_dict['Place.testing_storage'])

        def testing_all(self):
                ''' testing retrieval of objects '''
                test_dict = {'id': 'testing_retrieval',
                             'created_at': '2018-06-08T19:45:36.469639',
                             'updated_at': '2018-06-08T19:45:36.469672',
                             'test_attribute': 'still_arbitrary'}
                c = BaseModel(**test_dict)
                d = Review(**test_dict)
                all_objects = models.storage.all()

                self.assertEqual(all_objects['BaseModel.testing_retrieval'].__dict__,
                                 c.__dict__)

                self.assertEqual(all_objects['Review.testing_retrieval'].__dict__,
                                 d.__dict__)