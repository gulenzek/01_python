# -*- --coding:utf-8 -*-
# @author: gulenzek
"""
deque1.py
"""

from collections import deque

q1 = deque()

q1.append(1)
q1.append(2)
q1.append(3)


item1 = q1.pop()
print()

item1 = q1.popleft()
print()
