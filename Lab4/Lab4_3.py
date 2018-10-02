import math

def sum_to(n):
    sum=0
    for x in range(1,n+1):
        sum=sum+x

    return sum


print("Program to find the sum of number till n ")
n=int(input("Enter a number n : "))

result = sum_to(n)
print(result)