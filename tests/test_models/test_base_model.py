#!/usr/bin/env python3
''' unit testing for base class '''

import unittest
from models.base_model import BaseModel


class Test_Base_model(unittest.TestCase):
        ''' class for testing Base Model '''

        def test_attribute_creation(self):
                ''' testing that instance initializes with correct
                attributes '''
                a = BaseModel()
                self.assertTrue('id' in a.__dict__)
                self.assertTrue('created_at' in a.__dict__)
                self.assertTrue('updated_at' in a.__dict__)

        def test_update(self):
                ''' testing that updated_at is updated automatically
                with changes '''
                b = BaseModel(sandwich='grilled cheese')
                self.assertEqual(b.sandwich, 'grilled cheese')
                prev_update = b.updated_at
                b.sandwich = 'ham and cheese'
                self.assertNotEqual(b.updated_at, prev_update)

        def test_str(self):
                ''' testing BaseModel's __str___ '''
                c = BaseModel(id='my_id')
                self.assertEqual(c.__str__[:19], '[BaseModel] (my_id)')


if __name__ == '__main__':
    unittest.main()
