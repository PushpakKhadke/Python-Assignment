"""
8. Write a python program to create a function that accepts a string and calculate the
number of upper case letters and lower case letters.
"""

def Up_Low(My_String):
    Upper_Case=0
    Lower_Case=0
    print("String is : ",My_String)
    for e in My_String:
        if e.islower():
            Lower_Case+=1
        elif e.isupper():
            Upper_Case+=1
        else:
            pass #I added an extra case for the rest of the chars that aren't lower non upper
    print("Upper case characters in string : ",Upper_Case)
    print("Lower case characters in string : ",Lower_Case)
Up_Low("Hello Welcome To Python Course")