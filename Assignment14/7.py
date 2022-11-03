#  7. Write a Python script to remove all non int values from a list.

List=[1,2,3+4j,'Java','True',9.89]
print(List)
List1 = []
for i in List:
    if type(i)==int:

        List1.append(i)
List = List1
print(List)
