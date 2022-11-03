"""
5. Write a recursive python function to print first N even natural numbers.
"""

def Even_Natural_Number(Number):
    if Number>0:
        Even_Natural_Number(Number-1)
        print(2*Number,end=" ")
Even_Natural_Number(int(input("Enter how many even natural number you want print : ")))
