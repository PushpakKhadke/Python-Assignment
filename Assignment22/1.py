"""
1. Write a recursive python function to calculate sum of first N natural numbers
"""

def Recursive_Sum(num,sum):
    if num:
        sum+= num
        num-=1
        return Recursive_Sum(num,sum)
    return sum
Number = int(input("Enter the number : "))
print("Sum of first ",Number," natural numbers are : ")
print(Recursive_Sum(Number,0))