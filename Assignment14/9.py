"""
9. Write a Python script to print indices of all occurrences of a given element in a given
list.
"""

List = [1, 2, 2, 3, 2, 45]
print(List)
Fre = 0
Number = int(input("Enter The Number Which Is Vailiable In List: "))
for i in List:
    if (Number== i):
        print("Index No: ", Fre)
    Fre += 1

else:
    print(List)