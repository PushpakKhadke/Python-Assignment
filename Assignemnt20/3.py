"""
3. Write a python program to create a function that prints the even numbers from a
given list.
Sample List : [1, 2, 3, 4, 5, 6, 7, 8, 9]
"""

def Even_Number_List(l):
  Even_Number = []
  for i in l:
      if i % 2 == 0:
        Even_Number.append(i)
  return Even_Number
print(Even_Number_List([1, 2, 3, 4, 5, 6, 7, 8, 9]))