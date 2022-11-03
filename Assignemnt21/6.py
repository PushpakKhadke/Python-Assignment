"""
6. Write a recursive python function to print first N even natural numbers in reverse
order.
"""

def Even_Natural_Number_Reverse(Number):
    if Number>0:
        print(2 * Number, end=" ")
        Even_Natural_Number_Reverse(Number-1)

Even_Natural_Number_Reverse(int(input("Enter how many even  natural number in reverse order you want print : ")))
