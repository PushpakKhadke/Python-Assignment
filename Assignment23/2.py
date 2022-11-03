"""
2. Create a generator to produce first n odd natural numbers
"""

def odd_number_generator(number):
    a=1
    while number:
        yield a
        a+=2
        number-=1
for e in odd_number_generator(int(input("Enter how many odd_number you want print :"))):
    print(e,end=" ")
