"""
7. Write a python program to access a function inside a function.
"""

def make_add(a):
    def adder(b):
        c=a+b
        print(c)
    adder(5)
make_add(100)


""""
2nd Way!

def make_add(a):
    def adder(b):
        return a+b
    return adder
c=make_add(10)
print(c(10))
"""