"""
4. Write a recursive python function to print first N odd natural numbers in reverse order
"""

def  Odd_Natural_Number_Reverse(Number):
    if Number == 1:
        print(1)
    else:
        print(2*Number-1,end=" ")
        Odd_Natural_Number_Reverse(Number-1)
Odd_Natural_Number_Reverse(int(input("Enter how many odd natural number in reverse order you want print : ")))
