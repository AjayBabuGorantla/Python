import math

number  = int(input("Enter a positive integer : "))
count=0
for x in range(2,number+1):
    if(number%x==0):
        for y in range(2,x+1):
            if(pow(y,2)==x):
                count+=1
if(count==0):
    print("",number," is a square - free number ")
else:
    print("",number," is not a square - free number ")
