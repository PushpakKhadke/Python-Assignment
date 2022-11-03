"""
5. Write a python program to create a function to find the Min of three numbers.
"""

def Min_of_Three_Number():
    First_Number=int(input("Enter The First Number: "))
    Second_Number = int(input("Enter The Second Number: "))
    Third_Number = int(input("Enter The Third Number: "))
    if First_Number<Second_Number and First_Number<Third_Number:
        print("Smallest Number : ",First_Number)
    elif Second_Number<First_Number and Second_Number<Third_Number:
        print("Smallest Number : ",Second_Number)
    elif Third_Number<First_Number and Third_Number<Second_Number:
        print("Smallest Number : ",Third_Number)
Min_of_Three_Number()
