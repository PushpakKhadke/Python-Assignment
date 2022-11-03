"""
5. Create a generator to produce first n terms of Fibonacci series
"""

def Fibonacci_series(number):
    a,b=0,1
    while number:
        yield a
        a,b=b,a+b
        number-=1
for e in Fibonacci_series(int(input("Enter a number :"))):
    print(e,end=" ")
