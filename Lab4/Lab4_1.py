import math

def is_multiple(n,m):
    if(n%m==0):
        print("True")
    else:
        print("False")

print("Program to check if n is a multiple of m i.e n=mi, for some integer i ")
a=int(input("Enter the value of n : "))
b=int(input("Enter the value of m : "))

is_multiple(a,b)

