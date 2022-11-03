"""
7. Write a recursive python function to calculate sum of the digits of a given number
"""

def sum_of_digit(Number):
    if Number == 0:
        return 0
    return (Number%10 + sum_of_digit(int(Number/10)))
# Number = int(input("Enter number: "))
Number=12345
digit_sum = sum_of_digit(Number)
print("Sum Of Digit Of Number %d is : %d" % (Number,digit_sum))
