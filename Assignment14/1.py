# 1. Write a Python script to create a list of first N natural numbers.


Number = int(input("Enter How Many Natural Number You Want To Enter : "))
Natural_Number_List = list(range(1,Number+1))
print(Natural_Number_List)
print(type(Natural_Number_List))




"""
2nd Way!

Number = int(input("Enter How Many Natural Number You Want To Enter: "))
List=[]
for i in range(1,Number+1,1):
    List.append(i)
else:
    print(List)
"""




















# n = int(input("enter how natural number you want to enter -> "))
# list = []
# for i in range(1, n + 1, 1):
#     list.append(i)
# else:
#     print(list)
