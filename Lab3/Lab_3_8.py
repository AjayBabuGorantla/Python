import math

def digital_root(n):
    sum =0
    count =0
    while(n!=0):
        remainder=n%10
        sum = sum+remainder
        n=n//10
    temp =sum
    if(temp%10!=temp):
        return digital_root(temp)
    else:
        return temp


number = int(input("Enter a positive integer : "))

print("The digital root of ",number,"is ",digital_root(number))



#digital_root_sum =0
#temp = number
