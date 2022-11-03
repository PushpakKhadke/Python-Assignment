"""
2. Write a recursive python function to calculate sum of first N odd natural numbers
"""

def sum_odd_n(num,sum):
    if num:
        sum+=2*num-1
        num-=1
        return sum_odd_n(num,sum)
    return sum
Number = int(input("Enter the number : "))
print("Sum of first ",Number," odd natural numbers are : ")
print(sum_odd_n(Number,0))
