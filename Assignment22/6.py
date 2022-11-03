"""
6. Write a recursive python function to calculate the factorial of a number.
"""

def Factorial_Number(Number):
    if (Number == 1 or Number == 0):
        return 1
    else:
        return (Number * Factorial_Number(Number - 1))
Number = int(input("Enter Number : "))
print("Number is :",Number)
print("Factorial of", Number,"is :",Factorial_Number(Number))
