"""
8. Write a recursive python function to print cubes of first N natural numbers
"""
def Cube_Of_Natural_Number(Number):
    if Number>0:
        Cube_Of_Natural_Number(Number-1)
        print("Cube of",Number,"is :",Number**3)
Cube_Of_Natural_Number(int(input("Enter how many number of cubes you want print : ")))
