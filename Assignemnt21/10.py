"""
10. Write a recursive python function to print a number in reverse order.
"""


# Reverse a number using recursion

def Reverse_Number(Number, Number1):
    if Number==0:
        return Number1
    else:
        return Reverse_Number(Number//10, Number1*10 + Number%10)
number = int(input("Enter Number : "))
Reversed_Number = Reverse_Number(number,0)
print("Reverse of %d is : %d" %(number, Reversed_Number))