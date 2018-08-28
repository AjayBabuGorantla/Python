import math

prime_count=0
number=2
while(prime_count<=25):
    count=0
    for x in range(1,number+1):
        if(number%x==0):
            count+=1
    if(count==2):
        prime_count+=1
        print(number,end=',')
    number+=1
