"""
5. Write a recursive python function to calculate sum of cubes of first N natural numbers
"""

def Cube_Sum(Number):
    Sum=0
    for i in range(Number+1):
        Sum+=i**3
    return Sum
Number=int(input("Enter Number : "))
print("Sum of cubes of first {} natural numbers is :".format(Number),Cube_Sum(Number))
