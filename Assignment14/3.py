# 3. Write a Python script to create a list of first N even natural numbers.

Number = int(input("Enter How Many Even Natural Number You Want To Enter : "))
List=[]
for i in range(2,Number*2+1,2):
    List.append(i)
else:
    print(List)


