"""
3. Write a recursive python function to print first N odd natural numbers
"""

def Odd_Natural_Number(Number, c=1):
    if c<=Number:
        print(2*c-1,end=" ")
        Odd_Natural_Number(Number,c+1)
Odd_Natural_Number(int(input("Enter how many odd natural number you want print : ")))

