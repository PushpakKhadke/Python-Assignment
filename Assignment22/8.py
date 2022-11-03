"""
8. Write a recursive python function to print binary of a given decimal number.
"""

def convertToBinary(Number):
   if Number > 1:
       convertToBinary(Number//2)
   print(Number % 2,end = '')
Decimal_Number = int(input("Enter the Decimal Number : "))
convertToBinary(Decimal_Number)
