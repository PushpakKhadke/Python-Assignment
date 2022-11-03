# 4. Write a Python script to find the greatest number in a given list of numbers.

List=[]
Number=int(input("Enter How Many Number You Want To Enter: "))
while Number:
    List.append(input("Enter Number: "))
    Number-=1
else:
    print(List)
    print("Greatest Number is :",max(List))


"""
2nd Way!

List = [1,2,3,4,5,6,7,8,9]
print(max(List))
"""