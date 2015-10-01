from kao_list import KaoList
import unittest

class first(unittest.TestCase):
    """ Test cases of first """
        
    def test_hasElement(self):
        """ Test that the element is returned when it exists """
        expected = 1
        l = KaoList([expected, 2, 3])
        self.assertEqual(expected, l.first)
        
    def test_noElement(self):
        """ Test that None is returned when the element does not exist """
        expected = None
        l = KaoList()
        self.assertEqual(expected, l.first)

class last(unittest.TestCase):
    """ Test cases of last """
        
    def test_hasElement(self):
        """ Test that the element is returned when it exists """
        expected = 1
        l = KaoList([2, 3, expected])
        self.assertEqual(expected, l.last)
        
    def test_noElement(self):
        """ Test that None is returned when the element does not exist """
        expected = None
        l = KaoList()
        self.assertEqual(expected, l.last)