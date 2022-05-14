from cmath import inf
from collections.abc import MutableMapping
import copy
import math, random
from operator import indexOf

class KeyError(Exception):
    pass

class SkipList(MutableMapping):
    # add additional slots as you need
    __slots__ = '_head', '_tail', '_n', '_h', '_list', '_floor'

    #------------------------------- nested _Node class -------------------------------
    class _Node:
        __slots__ = '_key', '_value', '_prev', '_next', '_below', '_above'

        """Lightweight composite to store key-value pairs as map items."""
        def __init__(self, k, v, prev=None, next=None, below=None, above=None):
            self._key = k
            self._value = v
            self._prev = prev
            self._next = next
            self._below = below
            self._above = above

        def __eq__(self, other):               
            if other == None:
                return False
            return self._key == other._key   # compare items based on their keys

        def __ne__(self, other):
            return not (self == other)       # opposite of __eq__

        def __lt__(self, other):               
            return self._key < other._key    # compare items based on their keys
        
        def cut_link(self):
            self._next, self._prev = None, None

    def __init__(self):
        """Create an empty map."""
        self._head = self._Node(-math.inf, None, None, None, None, None)   # Head: the first node in a skip list
        self._tail = self._Node(math.inf, None, None, None, None, None)    # Tail: the last node in a skip list
        self._head._next = self._tail         # Initially, there's no item -> head is directly linked to the tail
        self._n = 0                              # Initially, there's no item, so _n = 0
        self._h = 1                             # Initially, there's one linked-list floor.
        self._list = [self._head, self._tail]   # Initially, there are only head, tail in list.
        self._floor = [self._list]                        # Initially, there's only default list list.
        
    def __str__(self):
        script = ""
        for floor in self._floor:
        # for i in range(self._h):
            script = script + "["
            for node in floor:
            # for node in self._floor[i]:
                if node._key is math.inf:
                    script = script + str(node._key)
                    break
                script = script + str(node._key) + ", "
            script = script + "]\n"
        return script

    def __getitem__(self, k):
        """Return value associated with key k (raise KeyError if not found)."""
        for elem in self._floor[self._h-1]:
            if elem._key == k: return elem._value
        raise KeyError
   
    def __setitem__(self, k, v):
        """Assign value v to key k, overwriting existing value if present."""
        
        new_node = self._Node(k, v)
        base_list = copy.deepcopy(self._floor[self._h-1])

        chk = None
        for elem in base_list:
            if elem._key == k: chk = True
            else: chk = False

        ##### overwriting #####
        if chk == True:
            for floor in self._floor:
                for elem in floor:
                    if elem._key == k:
                        elem._value = v
        
        ##### insert #####
        # make the base list
        if chk == False:
            node = base_list[0]
            cnt = 1
            while node._next < new_node:
                node = node._next
                cnt += 1
            self.insert_between(k, v, node, node._next)
            base_list.insert(cnt, node._next)
            self._n = self._n + 1

        # apply base list in floor
        if len(self._floor[self._h-1]) == 2:
            self._floor.append(base_list)
            self._h = self._h + 1
        else: self._floor[self._h-1] = base_list
        
        # append the floor for random times
        new_height = self.get_random_height()
        
        buffer_list = copy.deepcopy(self._floor[self._h-2])
        
        node = buffer_list[0]
        cnt = 1
        while node._next < new_node:
            node = node._next
            cnt += 1
        self.insert_between(k, v, node, node._next)
        buffer_list.insert(cnt, node._next)
        
        for i in range(new_height):
            self._floor.insert(self._h-1, buffer_list)
            self._h = self._h + 1
        
    def __delitem__(self, k):
        """Remove item associated with key k (raise KeyError if not found)."""
        base_list = self._floor[self._h-1]
        del_node = self._Node(None, None)
        chk = None
        for elem in base_list:
            if elem._key == k:
                chk = True
                break
            else: chk = False
        
        if chk == True:
            for floor in self._floor:
                for elem in floor:
                    # deletion
                    if elem._key == k:
                        del_node = elem
                        prenode, postnode = elem._prev, elem._next
                        elem._prev, elem._next = None, None
                        prenode._next, postnode._prev = postnode, prenode
                        break
                if del_node in floor: floor.remove(del_node)
            
            cnt = 0
            for floor in self._floor:
                if len(floor) == 2:
                    cnt += 1

            self._floor = self._floor[cnt-1:]
            self._h = self._h - cnt + 1
            self._n = self._n - 1
                        
        elif chk == False: raise KeyError(f'{k} not found.')

    def __len__(self):
        """Return number of items in the map."""
        return self._n

    def __iter__(self):                             
        """Generate iteration of the map's keys."""
        # hint: iterate over the base height (where the nodes that node._below is None)

        # go down all the way to the bottom

        # yield node._key while node._next is not having math.inf as the key

        base_list = self._floor[self._h-1]

        for elem in base_list:
            if elem._key != -math.inf and elem._key != math.inf:
                yield elem._key

    def get_random_height(self):
        height = 0
        while random.choice([True, False]):
            height += 1
        return height
    
    def insert_between(self, k, v, predecessor, successor):
        """Add element e between two existing nodes and return new node."""
        newest = self._Node(k, v, predecessor, successor)      # linked to neighbors
        predecessor._next = newest
        successor._prev = newest
    
    def delete_node(self, node):
        prenode = self._Node(None, None)
        postnode = self._Node(None, None)

        prenode, postnode = node._prev, node._next
        node._prev, node._next = None, None
        prenode._next, postnode._prev = postnode, prenode