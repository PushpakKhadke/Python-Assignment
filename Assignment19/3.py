"""
3. Write a python program to create a function which expects an unknown number of
arguments.
"""
def Function1(*args):
    return (len(args))
Function2 = Function1(1,2,3,4,5,6,7,8,9)
print("Number of arguments : ",Function2)
