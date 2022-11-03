"""
Write a recursive python function to print octal of a given decimal number.
"""

s = 1
octal = 0
def Decial_to_Octal(Number):
    global s , octal
    if Number !=0:
        octal = octal + (Number % 8) * s
        s = s * 10
        Decial_to_Octal(Number//8)
    return octal
Number = int(input("Enter the Decimal Value : "))
print("Octal Value of Decimal Number is : ",Decial_to_Octal(Number))