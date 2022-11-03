"""
5. Write a python program to add items from another set to the current set.
thisset ={"Java", "Python", "SQL"}
secondset= {"C", "Cpp", "NoSQL"}
"""

thisset1 ={"Java", "Python", "SQL"}
thisset2= {"C", "Cpp", "NoSQL"}
thisset1.update(thisset2)
print(thisset1)
print(type(thisset1))


