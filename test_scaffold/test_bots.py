import bots
import unittest

class Test_Values(unittest.TestCase):
    
    def test_dtype_init(self):
        """GOAL: test that all methods will output their appropriate data types"""
        self.assertEqual(type(bots.name)==str)
        
        pass