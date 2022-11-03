"""
Write a python program to create a function that finds a maximum of four numbers.
"""

def Maximum_of_four_number():
    First_Number = int(input("Enter Firs Number: "))
    Second_Number = int(input("Enter Second Number: "))
    Third_Number = int(input("Enter Third Number: "))
    Fourth_Number = int(input("Enter Fourth Number: "))

    #Cndition for First_Number
    if First_Number > Second_Number and First_Number > Third_Number and First_Number > Fourth_Number:
        print(First_Number)

    # Condition for Second_Number
    elif Second_Number > Third_Number and Second_Number > Fourth_Number and Second_Number > First_Number:
        print(Second_Number)

    # Condition for Third_Number
    elif Third_Number > Fourth_Number and Third_Number > First_Number and Third_Number > Second_Number:
        print(Third_Number)

    # Condition for Fourth_Number
    elif Fourth_Number > First_Number and Fourth_Number > Second_Number and Fourth_Number > Third_Number:
        print(Fourth_Number)
Maximum_of_four_number()

"""
2nd Way! 

def Maximum(Numbers):
    Max = 0
    for item in Numbers:
        if item > Max:
            Max  = item
    return print("Maximum Number is : ",Max)
print(Maximum([10,20,30,40]))
"""