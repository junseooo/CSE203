from collections import deque
from hashlib import new


class EmptyException(Exception):
   """Raised when the data structure is empty"""
   pass

class Deque: # Space used: O(n)
    # Always start nfrom initial capacity=2. Resize if needed.
    DEFAULT_CAPACITY = 2
    
    def __init__(self, capacity=DEFAULT_CAPACITY):
        self._data = [None]*capacity
        self._f = 0
        self._r = 0
        
    def __str__(self):
        # print(f'DEQUE({len(self)}: {self._data} / {self._f}, {self._r} / {self._data[self._f]}, {self._data[self._r]}]')
        return f'DEQUE({len(self)}: {self._data} / {self._f}, {self._r} / {self._data[self._f]}, {self._data[self._r]} / {self.N()}, {abs(self._r - self._f + 1)}]'

    # @property
    def N(self):
        return len(self._data)
    
    def __len__(self): # O(1)
        return len(self._data)

    def is_empty(self): # O(1)
        if self._f == self._r:
            return True
        return False
    
    def is_full(self):
        if ((self._r + 1) % self.N()) == self._f:
            return True
        return False
    
    def first(self): # O(1)
        if self.is_empty():
            raise EmptyException("Deque is Empty")
        front = (self._f + 1) % self.N()
        return self._data[front]
    
    def last(self):
        if self.is_empty():
            raise EmptyException("Deque is Empty")
        return self._data[self._r]

    def add_first(self, e): # O(1)*
        if self.is_full():
            self._data = self._resize(self.N())
        self._data[self._f] = e
        self._f = (self._f - 1 + self.N()) % self.N()

    def add_last(self, e): # O(1)*
        if self.is_full():
            self._data = self._resize(self.N())
        self._r = (self._r + 1) % self.N()
        self._data[self._r] = e

    def delete_first(self):   # O(1)*
        if self.is_empty():
            raise EmptyException("Deque is empty")

        front = (self._f + 1) % self.N()
        tmp = self._data[front]
        self._data[front] = None
        self._f = front

        lsize = abs(self._r - self._f + 1)
        if lsize < self.N()/2:
            self._data = self.del_resize(self.N())
        
        return tmp

    def delete_last(self):
        if self.is_empty():
            raise EmptyException("Deque is Empty")
            
        tmp = self._data[self._r]
        self._data[self._r] = None
        rear = (self._r - 1 + self.N()) % self.N()
        self._r = rear
        
        lsize = abs(self._r - self._f + 1)
        if lsize < self.N()//2:
            self._data = self.del_resize(self.N())

        return tmp
        
    def _resize(self, cap): # O(n)
        if self.is_full:
            empty_list = [None] * (2*cap)
            for i in range(cap):
                empty_list[i] = self._data[(self._f + i) % self.N()]
            self._f = 0
            self._r = cap - 1
            return empty_list
    
    def del_resize(self, cap):
        empty_list = [None] * cap
        for i in range(cap//2):
            empty_list[i] = self._data[(self._f + i) % self.N()]
        self._f = 0
        self._r = cap//2 - 2
        empty_list = empty_list[:(cap//2)]
        return empty_list