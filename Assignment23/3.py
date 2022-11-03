"""
3. Create a generator to produce first n even natural numbers
"""

def even_number_generator(number):
    x=2
    while number:
        yield x
        x+=2
        number-=1
for e in even_number_generator(int(input("Enter the number :"))):
    print(e,end=" ")