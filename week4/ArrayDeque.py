class EmptyException(Exception):
   """Raised when the data structure is empty"""
   pass

class Deque: # Space used: O(n)
    # Always start from initial capacity=2. Resize if needed.
    DEFAULT_CAPACITY = 2
    
    def __init__(self, capacity=DEFAULT_CAPACITY):
        self._data = [None]*capacity
        self._f = 0
        self._r = 0
        
    def __str__(self):
        print(f'DEQUE({len(self)}: {self._data} / {self._f}, {self._r}')

    @property
    def N(self):
        # IMPLEMENT HERE
    
    def __len__(self): # O(1)
        # IMPLEMENT HERE

    def is_empty(self): # O(1)
        # IMPLEMENT HERE

    def add_first(self, e): # O(1)*
        # IMPLEMENT HERE

    def first(self): # O(1)
        # IMPLEMENT HERE

    def delete_first(self):   # O(1)*
        # IMPLEMENT HERE
    
    def add_last(self, e): # O(1)*
        # IMPLEMENT HERE

    def last(self):
        # IMPLEMENT HERE

    def delete_last(self):
        # IMPLEMENT HERE
        
    # Use doubling strategy for resizing the buffer.
    def _resize(self, cap): # O(n)
        # IMPLEMENT HERE