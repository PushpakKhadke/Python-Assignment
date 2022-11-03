"""
10. Write a recursive python function to find the Nth term of the Fibonacci series.
"""

def Fibonacci_Series(Number):
    if Number==1:
        return 0
    elif Number==2:
        return 1
    else:
        return Fibonacci_Series(Number-1) + Fibonacci_Series(Number-2)
Term = int(input("Which term of Fibonacci series:"))
# a=10
Result = Fibonacci_Series(Term)
print("%dth term of Fibonacci series is : %d" %(Term, Result))
