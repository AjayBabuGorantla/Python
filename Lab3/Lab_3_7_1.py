import math

number=1
SquareFreeNumber_count = 0

while(SquareFreeNumber_count<=25):
    for x in range(1,number+1):
        if(number%x==0):
            count=0
            for y in range(1,x+1):
                if(pow(y,2)==x):
                    count+=1
        number+=1
        if(count==0):
            print(number)
            SquareFreeNumber_count+=1
