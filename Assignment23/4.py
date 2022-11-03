"""
4. Create a generator to produce squares of first N natural numbers
"""

def squares_number_generator(number):
    a=1
    while number:
        yield a**2
        a+=1
        number-=1
for e in squares_number_generator(int(input("Enter how many odd_number you want print :"))):
    print(e,end=" ")