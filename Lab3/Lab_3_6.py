import math

def fibonacci(number):
    a,b = 0,1
    while(a<number):
        print(a,end=',')
        a,b =b,a+b

number =int(input("Enter the maximum number of the Fibonacci you want : "))
fibonacci(number)
