"""
3. Write a recursive python function to calculate sum of first N even natural numbers
"""

def Sum_Of_Even_Natural_Number(num,sum):
    if num:
        sum+=2*num
        num-=1
        return Sum_Of_Even_Natural_Number(num,sum)
    return sum
Number = int(input("Enter the number : "))
print("Sum of first ",Number," even natural numbers are : ")
print(Sum_Of_Even_Natural_Number(Number,0))