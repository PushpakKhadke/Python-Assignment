"""
6. Write a python program to create a function and print a list where the values are
square of numbers between 1 and 30.
"""


def Square_List():
    List = []
    for i in range(1,31):
        List.append(i*i)
    else:
        print(List)
Square_List()