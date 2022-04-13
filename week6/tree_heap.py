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
    
    def _swap(self, node1, node2):
        """Swap the elements at indices i and j of array."""
        # IMPLEMENT HERE
        buffer_node = self._Node(None, None, None, None)
        buffer_node = node1
        node1 = node2
        node2 = buffer_node

    def _upheap(self, node):
        # IMPLEMENT HERE
        while node._element < node._parent._element:
            self._swap(node, node._parent)
        
    def _downheap(self, node):
        # IMPLEMENT HERE
        while node._element > min(node._left._element, node._right._element):
            buffer_node = self._Node(None, None, None, None)
            if node._left._element < node._right._element:
                buffer_node = node._left
            elif node._left._element > node._right._element:
                buffer_node = node._right
            self._swap(node, buffer_node)
    
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

    def add(self, key):
        """Add a key to the priority queue."""
        # IMPLEMENT HERE
        new_node = self._Node(key, None, None, None)
        if self.is_empty(): # empty tree
            self._root = new_node
            self._last = self._root
        elif self._last is self._root:
            self._root._left = new_node
            new_node._parent = self._root
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
                            self.add_left(buffer_node, new_node)
                        break
                    buffer_node = buffer_node._parent

                # next node's parent is buffer_node

        self._last = new_node
        self._size += 1

    # def add(self, key):
    #     """Add a key to the priority queue."""
    #     # IMPLEMENT HERE
    #     new_node = self._Node(key, None, None, None)
    #     if self.is_empty(): # empty tree
    #         self._root = new_node
    #         self._last = self._root
    #     elif self._size == 1:
    #         self._root._left = new_node
    #         new_node._parent = self._root
    #     else: # unempty tree
    #         buffer_node = self._last
    #         while buffer_node._parent is not self._root:
    #             buffer_node = buffer_node._parent
    #             if buffer_node._right is None:
    #                 buffer_node._right = new_node
    #                 new_node._parent = buffer_node
    #                 break
    #             else:
    #                 if buffer_node._right._left is None:
    #                     buffer_node._right._left = new_node
    #                     new_node._parent = buffer_node._right
    #                     break
        
    #     self._last = new_node
    #     self._size += 1

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

        self._swap(self._root, self._last)
        self._last._parent = None
        self._downheap(self._root)
        return self._last._element

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

th = TreeHeap()
# for i in range(7):
#     th.add(7-i)
th.add(1)
th.add(2)
th.add(3)
th.add(4)
th.add(5)
th.add(6)
th.add(7)
th.add(8)
th.add(9)
th.add(10)
th.add(11)
th.add(12)
th.add(13)

th.display()