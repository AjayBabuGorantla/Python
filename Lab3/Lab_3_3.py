import math
for number in range(1,30000):
    sum = 0
    temp=number
    while(number!=0):
        remainder = number%10
        sum = sum + math.factorial(remainder)
        number = number//10
    if(temp==sum):
        print("",temp,"is a strong number ")
