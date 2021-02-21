# -*- --coding:utf-8 -*-
# @author: gulenzek
"""
decorators1.py
"""
def greet():
    print("Greetings!")

def do_twice(func): #bir değişken
    def inner():
        func()
        func()
    return inner


greet2 = do_twice(greet)
print(greet2)

@do_twice()
def greet():
    print("Greetings!")

greet()
if __name__ == "__main__":
    main()


# -*- coding: utf-8 -*-
"""
decorators1.py
"""

def greet():
    print("greetings")

def do_twice(func):
    def inner():
        func()  # greet()
        func()  # greet()
    return inner

# greet2 = do_twice(greet)
# print(greet2)  # <function do_twice.<locals>.inner at 0x000001D4FEAEC280>
# greet2()

greet = do_twice(greet)
greet()

# syntactic sugar:
# sadece 19. satirin yerine, @do_twice yazabiliriz:
@do_twice
def greet():
    print("greetings")

greet()
