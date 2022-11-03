# 4. Write a python program to Swap two tuples in Python.

tuple1 = (1,2,3)
tuple2 = (2,3,4)
print("Before Swapping:")
print(tuple1)
print(tuple2)
temp = tuple1
tuple1 = tuple2
tuple2 = temp
print()
print("After Swapping:")
print(tuple1)
print(tuple2)

"""
2nd!  Logic

tuple1 = (1,2,3)
tuple2 = (2,3,4)
print("Before Swapping:")
print(tuple1)
print(tuple2)
tuple1,tuple2 = tuple2,tuple1
print()
print("After Swapping:")
print(tuple1)
print(tuple2)
"""
