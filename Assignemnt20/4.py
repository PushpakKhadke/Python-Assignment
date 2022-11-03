"""
4. Write a python program to create a function that checks whether a passed string is
palindrome or not.
"""

def String_Palindrome(My_String):
    My_String = My_String.casefold()
    # reverse the string
    Rev_String = reversed(My_String)
    #   check if the string is equal to its reverse
    if list(My_String) == list(Rev_String):
        print("The string is a palindrome.")
    else:
        print("The string is not a palindrome.")
String_Palindrome('aIbohPhoBiA')









