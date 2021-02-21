# -*- coding: utf-8 -*-
"""
stack1.py
last in, first out
LIFO
https://docs.python.org/3/tutorial/datastructures.html#using-lists-as-stacks
"""

class Stack:
    def __init__(self):
        self._stack = []

    def push(self, value):
        self._stack.append(value)

    def pop(self):
        return self._stack.pop()

    def __str__(self):
        return str(self._stack)

stack1 = Stack()
stack1.push(1)
stack1.push(2)
stack1.push(3)
item1 = stack1.pop()
print(item1)  # 3
print(stack1)
