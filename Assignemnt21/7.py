"""
7. Write a recursive python function to print squares of first N natural numbers
"""

def Square_Of_Natural_Number(Number):
    if Number>0:
        Square_Of_Natural_Number(Number-1)
        print("Square of",Number,"is :",Number**2)
Square_Of_Natural_Number(int(input("Enter how many number of squares you want print : ")))
