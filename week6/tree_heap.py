class Empty(Exception):
  """Error attempting to access an element from an empty container."""
  pass

class TreeHeap:
    __slots__ = '_root', '_last', '_size'

    #-------------------- nonpublic
    class _Node:
        __slots__ = '_element', '_left', '_right', '_parent'

        def __init__(self, element, left, right, parent):
            self._element = element
            self._left = left
            self._right = right
            self._parent = parent

        def is_left_child(self, node):
            if self._parent._left is node: return True
            return False
        
        def change_with_parent(self):
            self._element, self._parent._element = self._parent._element, self._element            
        
    def _swap(self, node1, node2):
        """Swap the elements at indices i and j of array."""
        # IMPLEMENT HERE
        node1, node2 = node2, node1
        return

    def _upheap(self, node): # when node is entering, we need to compare between node and node's parent. and repeat until node is larger than node's parent
        # IMPLEMENT HERE
        min_node = self._Node(None, None, None, None)
        min_node = node
        while min_node is not self._root:
            if min_node._element < min_node._parent._element:
                min_node.change_with_parent()
            min_node = min_node._parent
        return

    def _downheap(self, node): # entered node is changed root node
        # IMPLEMENT HERE
        buffer_node = self._Node(None, None, None, None)
        buffer_node = node
        
        while 1:
            if buffer_node._left is None: break
            elif buffer_node._right is None:
                if buffer_node._element > buffer_node._left._element:
                    buffer_node._left.change_with_parent()
                    break
            elif buffer_node._element < min(buffer_node._left._element, buffer_node._right._element): break
            else: # right and left is not empty and buffer is larger than right and left
                # if buffer_node._element >= min(buffer_node._left._element, buffer_node._right._element):
                    min_node = self._Node(None, None, None, None)
                    if buffer_node._left._element < buffer_node._right._element:
                        min_node = buffer_node._left
                        buffer_node = min_node
                        min_node.change_with_parent()
                    elif buffer_node._left._element > buffer_node._right._element:
                        min_node = buffer_node._right
                        buffer_node = min_node
                        min_node.change_with_parent()

        return
    
    #-------------------- public
    def __init__(self):
        """Create a new empty Priority Queue."""
        self._root = None
        self._last = None
        self._size = 0

    def __len__(self):
        """Return the number of items in the priority queue."""
        return self._size

    def is_empty(self):
        return self._size == 0

    def add_right(self, parent, child):
        parent._right = child
        child._parent = parent
    
    def add_left(self, parent, child):
        parent._left = child
        child._parent = parent
    
    def change_with_root(self, node): # element change
        node._element, self._root._element = self._root._element, node._element

    def add(self, key):
        """Add a key to the priority queue."""
        # IMPLEMENT HERE
        new_node = self._Node(key, None, None, None)
        if self.is_empty(): # empty tree
            self._root = new_node
            self._last = self._root
        elif self._last is self._root: # just root
            self._root._left = new_node
            new_node._parent = self._root
            self._last = new_node
            self._upheap(self._last)
        else: # unempty tree
            if self._last is self._last._parent._left: # last's parent has empty right node
                self.add_right(self._last._parent, new_node)
            else: # last's parent has no empty child
                buffer_node = self._last
                while 1:
                    if buffer_node is self._root._left:
                        buffer_node = self._root._right
                        while buffer_node._left is not None:
                            buffer_node = buffer_node._left
                        self.add_left(buffer_node, new_node)
                        break
                    elif buffer_node is self._root._right:
                        buffer_node = self._root._left
                        while buffer_node._left is not None:
                            buffer_node = buffer_node._left
                        self.add_left(buffer_node, new_node)
                        break
                    elif buffer_node.is_left_child(buffer_node) is True:
                        if buffer_node._parent._right is None:
                            self.add_right(buffer_node, new_node)
                        else:
                            buffer_node = buffer_node._parent._right
                            while 1:
                                if buffer_node._left is None: break
                                buffer_node = buffer_node._left
                            self.add_left(buffer_node, new_node)
                        break
                    buffer_node = buffer_node._parent

            self._last = new_node
            self._upheap(self._last)
        self._size += 1

    def min(self):
        """Return but do not remove (k,v) tuple with minimum key.
        Raise Empty exception if empty.
        """
        if self.is_empty():
            raise Empty('Heap is empty')
        return self._root._element

    def remove_min(self):
        """Remove and return the minimum key.
        Raise Empty exception if empty.
        """
        # IMPLEMENT HERE
        if self.is_empty():
            raise Empty('Heap is empty')

        elif self._last is self._root: # just root
            buffer_node = self._Node(None, None, None, None)
            min_node = self._root
            self._root = buffer_node
            return min_node._element
        
        else: # size(tree) > 1
            # store mininmun value(root element) for return value
            # change last node and root node
            # find next last index
            # remove last node
            # down heap of root node

            # store mininmun value(root element) for return value
            min_value = self._root._element

            # change last node and root node
            self.change_with_root(self._last)

            if self._size == 2:
                self._last._parent = None
                self._root._left = None
                self._last = self._root
                self._size -= 1

                return min_value

            else: # size > 2
                # find next last index
                buffer_node = self._last # buffer_node means next last index
                while 1:
                    if buffer_node is self._root._left:
                        buffer_node = self._root._right
                        while 1:
                            if buffer_node._right is None: break
                            buffer_node = buffer_node._right
                        break

                    elif buffer_node is self._root._right:
                        buffer_node = self._root._left
                        while buffer_node._right is not None:
                            buffer_node = buffer_node._right
                        break

                    elif buffer_node.is_left_child(buffer_node) is False:
                        buffer_node = buffer_node._parent._left
                        while 1:
                            if buffer_node._right is None: break
                            buffer_node = buffer_node._right
                        break

                    buffer_node = buffer_node._parent
                
                # print()
                # print()
                # self.display()
                
                # remove last node
                if self._last.is_left_child(self._last) is True:
                    self._last._parent._left = None
                else:
                    self._last._parent._right = None
                self._last._parent = None

                self._last = buffer_node

                
                self._downheap(self._root)
                
                # print()
                # print()
                # self.display()

                self._size -= 1

                return min_value

    def display(self):
        self._display(self._root, 0)

    def _display(self, node, depth):
        if node == None:
            return

        if node._right != None:
            self._display(node._right, depth+1)
        label = ''
        if node == self._root:
            label += '  <- root'
        if node == self._last:
            label += '  <- last'
        print(f'{"    "*depth}* {node._element}{label}')
        if node._left != None:
            self._display(node._left, depth+1)



import random

sequence = list(range(10))
random.shuffle(sequence)

sequence1 = [7, 9, 3, 2, 5, 4, 8, 1, 0, 6]
print(sequence1)
print()

# pq sort
th = TreeHeap()
for item in sequence:
    th.add(item)

th.display()

print(th.remove_min())
th.display()
print()
print()
print(th.remove_min())
print(th.remove_min())
print(th.remove_min())
print(th.remove_min())
print(th.remove_min())
th.display()
print()
print()
print(th.remove_min())
th.display()
print()
print()
# print(th.remove_min())
# print(th.remove_min())
# print(th.remove_min())

# while not th.is_empty():
#     print(th.remove_min())

# print(th.remove_min())
# th.display()
# print()
# print()

# print(th.remove_min())
# th.display()
# print()
# print()

# print(th.remove_min())
# th.display()
# print()
# print()

