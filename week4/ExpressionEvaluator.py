## DO NOT EDIT THIS CELLS
import re

# to_list: convert a string into list of operand and operators.
# expression: an expression in str, ex:'1+2/3*4-5*6'
# return: list of operand and operators from the str, ex: [1, '+', 2, '/', 3, '*', 4, '-', 5, '*', 6]
def to_list(expression):
    is_float = lambda x: x.replace('.','',1).isdigit() and "." in x
    L = re.split('([\-\+\/\*])', expression)
    for i in range(len(L)):
        if L[i].isnumeric():
            L[i] = int(L[i])
        elif is_float(L[i]):
            L[i] = float(L[i])
    return L

class EmptyException(Exception):
   """Raised when the data structure is empty"""
   pass

# Array-based stack implementation
class ArrayStack:
    def __init__(self):
        self._data = []
    def __len__(self):
        return len(self._data)
    def is_empty(self):
        return len(self) == 0
    def push(self, e):
        self._data.append(e)
    def top(self):
        if self.is_empty():
            raise EmptyException('Stack is empty')
        return self._data[-1]
    def pop(self):
        if self.is_empty():
            raise EmptyException('Stack is empty')
        return self._data.pop()

# Return the priority of operator
def priority(element):
    if element in ['-', '+']:
        return 1
    elif element in ['*', '/']:
        return 2

# identify whether the item is a number (=operand) or other (=operator)
# item: operand or operator (an item of a list converted by to_list)
# return: True if operand, False if operator
def is_number(item):
    return type(item) == int or type(item) == float

######################################################
# IMPLEMENT THE TWO METHODS BELOW
######################################################

def infix_to_postfix(L):
    
    # implement here

    s = ArrayStack()
    postfix = []
    for i in L:
        if is_number(i): # operand
            postfix.append(i)
        else: # operator
            if s.is_empty():
                s.push(i)
            else:
                while priority(s.top()) >= priority(i):
                    postfix.append(s.pop())
                    if s.is_empty():
                        break
                s.push(i)

    while s.is_empty() is False:
        postfix.append(s.pop())

    return postfix

def eval_postfix(L):
    s = ArrayStack()
    
    # implement here

    for i in L:
        if is_number(i): #operand
            s.push(i)
        else: #operator
            buf2 = s.pop()
            buf1 = s.pop()
            buf_res = []
            buf_res.append(str(buf1))
            buf_res.append(i)
            buf_res.append(str(buf2))
            buf_str = ''.join(buf_res)
            s.push(eval(buf_str))
    return s.pop()

#######################################################
# test code
#######################################################

# expression = to_list('1+2/3*4-5*6')
expression = to_list()
print(expression)
L = infix_to_postfix(expression)
print(L)
result = eval_postfix(L)
print(result)

# or in short, you may try this
print(eval_postfix(infix_to_postfix(to_list('1+2/3*4-5*6'))))
print(1+2/3*4-5*6)