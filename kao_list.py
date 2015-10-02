from kao_decorators import proxy_for
from smart_defaults import smart_defaults, PerCall

@proxy_for('_lst', ['__contains__', '__len__', '__getitem__', '__setitem__', '__iter__',
                    'append', 'index', '__repr__'])
class KaoList:
    """ Represents a list of items """
    
    @smart_defaults
    def __init__(self, lst=PerCall([])):
        """ Initialize with the list to wrap """
        self._lst = lst
        
    @property
    def first(self):
        """ Return the first element of the list """
        return self.get_index(0)
        
    @property
    def last(self):
        """ Return the first element of the list """
        return self.get_index(-1)
        
    def previous(self, item):
        """ Return the element that occurs before the given item """
        index = self.index(item)
        if index > 0:
            return self.get_index(index-1)
        else:
            return None
        
    def next(self, item):
        """ Return the element that occurs after the given item """
        index = self.index(item)
        return self.get_index(index+1)
        
    def get_index(self, index):
        """ Return the value at the given index or None """
        indexValue = index if index >= 0 else abs(index)-1
        return self[index] if indexValue < len(self) else None
        
    def __eq__(self, other):
        """ Return if this list is equal to another """
        return self._lst == other