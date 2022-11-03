"""
9. Write a python program to create a function to check whether a number falls in a
given range.
"""

def Test_Range(Number):
    if Number in range(3,9):
        print( Number,"is in the range")
    else :
        print("The number is outside the given range.")
Number1 = int(input("Enter The Number : "))
Test_Range(Number1)

