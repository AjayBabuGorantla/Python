import math

def is_even(n):
    if(n&1):
        print("False ( Not even )")
    else:
        print("True( It is even )")


n=int(input("Enter a number to check if it is even : "))

is_even(n)