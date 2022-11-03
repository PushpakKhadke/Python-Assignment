"""
7. Write a python program to sum all the numbers in a list.

"""
def Sum_of_Number_List(list):
    print(sum(list))
    return list
Sum_of_Number_List([2,1,8,10])

"""
2nd Way!

def Sum_of_Number_List():
    List = []
    Number=int(input("Enter number of elements: "))
    for i in range(0, Number):
        Elements = int(input())
        List.append(Elements)  # adding the element
    print(List)
    print("Sum all the numbers in a list.",sum(List))
Sum_of_Number_List()

"""