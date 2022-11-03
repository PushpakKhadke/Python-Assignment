"""
1. Write a python program to create a function that takes a list and returns a new list
with the original list's unique elements.
"""

def Unique_List(l):
    x = []
    for i in l:
        if i not in x:
            x.append(i)
    return x
print(Unique_List([2,2,3,3,3,3,3,4,5]))