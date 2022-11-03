"""
1. Write a recursive python function to print first N natural numbers.
"""

def Natural_Number(Number):
    if Number>0:
        Natural_Number(Number-1)
        print(Number,end=" ")
Natural_Number(int(input("Enter how many natural number you want print : ")))
