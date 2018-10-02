import math

def filter(list):
    count=0
    for i in range(0,len(list)):
        for j in range(0,len(list)):
            if(i==j):
                continue
            elif(list[i]==list[j]):
                count+=1
    return count




print("Enter the values for the list with spaces in between: ",sep="")
list=[int(x) for x in input().split()]
result= filter(list)
if(result==0):
    print("The numbers in the list are distinct ! ",sep="")
else:
    print("The numbers in the list are not distinct ! ", sep="")

print(list)



