import math

for number in range(100,201):
    count=0
    for x in range(1,number+1):
        if(number%x==0):
            count+=1
    if(count==2):
        print(number,end=',')
'''else:
    print("Not a prime")'''
 
