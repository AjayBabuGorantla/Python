def is_prime(x):
    if(x>2):
        for i in range(2,x):
            if(x%i==0):
                # print("It is not prime")
                return 0
        
        else:
            # print("It is prime")
            return 1
num = eval(input("Enter the number "))

l = list()
for i in range(3,num):
    if(is_prime(i)and(i%2!=0)):
        
        l.append(i)
for a in range(0,l.__len__()):
    for n in range(0,l.__len__()):
        sum = l.__getitem__(a) + l.__getitem__(n)
        if(sum ==num and (l.__getitem__(a)<l.__getitem__(n))):
            
            print(l.__getitem__(a)," ",l.__getitem__(n),end="\n")
            
            
        

