from kao_decorators import proxy_for
from smart_defaults import smart_defaults, PerCall

@proxy_for('_lst', ['__contains__', '__len__', '__getitem__', '__setitem__', '__iter__',
                    'append', 'index'])
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
        return self.get_index(index-1)
        
    def get_index(self, index):
        """ Return the vlaue at the given index or None """
        return self[index] if abs(index) < len(self) else None