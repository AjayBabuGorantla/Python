import math
import copy

def mode(list):
    count_list=[]


    for i in range(0,len(list)):
        count=1
        for j in range(i+1,len(list)):
            if(list[i]==list[j]):
                count+=1
        count_list.insert(i,count)
    #print(count_list)

    sorted_count_list=sorted(count_list)
    #print(sorted_count_list)
    sorted_count_list.reverse()
    #print(sorted_count_list)

    print("The modes are :",end="")
    for i in range(0,len(count_list)):
        if(count_list[i]==sorted_count_list[0]):
            mode=list[i]
            print(mode,end=" ")

list=[int(x) for x in input().split()]
mode(list)
print()
print("The entered list is : ",list)