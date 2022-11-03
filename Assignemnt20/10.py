"""
10. Write a python program to create a function to check whether a string is an anagram
or not.
"""


def Anagram():
    String1 ="listen"
    String2 ="silent"
    a=sorted(String1)
    b=sorted(String2)
    print("Sorted String1 :",a)
    print("Sorted String2 :",b)
    print()
    if sorted(String1)==sorted(String2):
        print("The Strings Are Anagrams")
    else:
        print("The Strings Are Not  Anagrams")
Anagram()

