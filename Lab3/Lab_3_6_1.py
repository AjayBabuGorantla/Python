import math

def fibonacci():
    a,b = 0,1
    count=0
    while(count<25):
        print(a,end=',')
        a,b =b,a+b
        count+=1

#number =int(input("Enter the maximum number of the Fibonacci you want : "))
fibonacci()
