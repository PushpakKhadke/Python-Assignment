"""
2. Write a Python script to create a list of first N odd natural numbers.
"""

Number = int(input("Enter How Many Odd Natural Number You Want To Enter : "))
List=[]
for i in range(1,Number*2,2):
    List.append(i)
else:
    print(List)




