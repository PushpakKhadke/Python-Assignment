"""
2. Write a recursive python function to print first N natural numbers in reverse order
"""

def Reverse_Natural_Number(Number):
    if Number>0:
        print(Number,end=" ")
        Reverse_Natural_Number(Number-1)
Reverse_Natural_Number(int(input("Enter how many natural number in reverse order you want print : ")))
