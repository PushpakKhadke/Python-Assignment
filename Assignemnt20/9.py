"""
9. Write a python program to create a function to check whether a string is a pangram
or not.
"""

def Is_Pangram(String):
    Alphabet = "abcdefghijklmnopqrstuvwxyz"
    for e in Alphabet:
        if e not in String.lower():
            return False
    return True
string = 'the quick brown fox jumps over the lazy dog'
if (Is_Pangram(string) == True):
    print("Yes")
else:
    print("No")
print()


"""
2nd Way!

def Is_Pangram(String):
    for e in String:
        if e in String.lower():
            print("Yes")
            break
        elif e not in String.lower():
            print("Not")
            break
        else:
            pass
Is_Pangram("abcdefghijklmnopqrstuvwxyz")
"""