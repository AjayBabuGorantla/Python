def d(x):
    sum=0
    for i in range(1,x):
        if(x%i==0):
            sum=sum + i
    return sum
l = list()

for i in range(1,10001):
    l.append(d(i))
for i in range(1,10001):
    if(l.__contains__(i)):
        x=d(i)
        if(d(x)==i and (x!=i)):
            print("The amicable pairs are {},{}".format(i,d(i)))

    
    
