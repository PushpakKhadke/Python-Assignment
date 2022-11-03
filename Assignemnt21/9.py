"""
9. Write a recursive python function to print first N multiples of a given number.
"""


def Multiples_Of_Number(Number, Number_Multiples):
    if Number_Multiples <= 0:
        print(end = " ")
    else:
        print(Number,end=" ")
        Multiples_Of_Number(Number+Number,Number_Multiples-1)

Multiples_Of_Number(1,10)
