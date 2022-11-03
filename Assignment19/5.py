"""
5. Write a python program to create a function which expects a list as an argument.
"""

def Function1(a):
    print(a)
Function1(a=[1,2,3,4,5])




def My_Function(*l):
  for x in l:
    print(x)
Numbers = [1,2,3,4,5]
My_Function(Numbers)
