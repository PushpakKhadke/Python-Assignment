"""
2. Write a python program to create a function that takes a number as a parameter and
checks if the number is prime or not.
"""

def Prime_Number_Check(Number):

    # Number=int(input("Enter The Number: "))
    for i in range(2,Number):
        if Number%i==0:
            print("Not Prime Number")
            break
    else:
        print("Prime Number")
Prime_Number_Check(97)
