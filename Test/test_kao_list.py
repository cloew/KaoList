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

class previous(unittest.TestCase):
    """ Test cases of previous """
        
    def test_hasPrevious(self):
        """ Test that the previous element is returned when it exists """
        expected = 1
        item = 2
        l = KaoList([expected, item])
        self.assertEqual(expected, l.previous(item))
        
    def test_noItem(self):
        """ Test that the proper error is thrown when the item is not in the list """
        item = 2
        l = KaoList()
        self.assertRaises(ValueError, l.previous, item)
        
    def test_noPrevious(self):
        """ Test that None is returned when there is no previous item in the list """
        expected = None
        item = 2
        l = KaoList([item, 1])
        self.assertEqual(expected, l.previous(item))

class next(unittest.TestCase):
    """ Test cases of next """
        
    def test_hasNext(self):
        """ Test that the next element is returned when it exists """
        expected = 1
        item = 2
        l = KaoList([item, expected])
        self.assertEqual(expected, l.next(item))
        
    def test_noItem(self):
        """ Test that the proper error is thrown when the item is not in the list """
        item = 2
        l = KaoList()
        self.assertRaises(ValueError, l.next, item)
        
    def test_noNext(self):
        """ Test that None is returned when there is no next item in the list """
        expected = None
        item = 2
        l = KaoList([1, item])
        self.assertEqual(expected, l.next(item))