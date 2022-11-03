"""
4. Write a recursive python function to calculate sum of squares of first N natural
numbers
"""

def Cube_Sum(Number):
    Sum=0
    for i in range(Number+1):
        Sum+=i**2
    return Sum
Number=int(input("Enter Number : "))
print("Sum of Squares of first {} natural numbers :".format(Number),Cube_Sum(Number))
