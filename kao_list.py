from kao_decorators import proxy_for
from smart_defaults import smart_defaults, PerCall

@proxy_for('_lst', ['__contains__', '__len__', '__getitem__', '__setitem__', '__iter__'])
class KaoList:
    """ Represents a list of items """
    
    @smart_defaults
    def __init__(self, lst=PerCall([])):
        """ Initialize with the list to wrap """
        self._lst = lst
        
    @property
    def first(self):
        """ Return the first element of the list """
        return self[0] if len(self) > 0 else None
        
    @property
    def last(self):
        """ Return the first element of the list """
        return self[-1] if len(self) > 0 else None