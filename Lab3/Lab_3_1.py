import math

number= int(input("Enter a positiver integer : "))

sum=0

for divisor in range(1,number):
    if(number%divisor==0):
        sum=sum+divisor
if(sum==number):
    print("The number is a Perfect Number ")
elif(sum<number):
    print("The number is a Deficient Number ")
else:
    print("The number is a Abundant Number ")
