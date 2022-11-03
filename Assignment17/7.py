"""
7. Write a python program to remove last item of the given set
thisset = {"Python", "Django", "JavaScript", “SQL”}
"""

thisset = {"Python", "Django", "JavaScript", "SQL"}
print("Orignal Set")
print(thisset)
thisset=list(thisset)
thisset.pop()
thisset=set(thisset)
print()
print("Remove set")
print(thisset)

"""
2nd Way!

thisset = {"Python", "Django", "JavaScript", "SQL"}
thisset.remove("SQL")
print(thisset)
"""


