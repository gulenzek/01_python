# -*- coding: utf-8 -*-
"""
decorators2.py
"""
import time


def measure_time(func):
    def inner(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        delta = end_time - start_time
        print(f"{delta} kadar sürdü.")
        return result
    return inner

# f1 = measure_time(f1)
@measure_time
def f1():
    print("begin f1()")
    time.sleep(3)
    print("end f1()")

f1()

@measure_time
def agir_topla(a, b):
    time.sleep(2)
    return a+b

# agir_topla = inner
toplam = agir_topla(2, 3)
print(toplam)
