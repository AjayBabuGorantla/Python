def is_prime(x):
    if(x>2):
        for i in range(2,x):
            if(x%i==0):
                # print("It is not prime")
                return 0
                
        else:
            # print("It is prime")
            return 1
l = list()
for i in range(100,200):
    if(is_prime(i)):
       
        l.append(i)
        
        
for j in range(0,l.__len__()-1):
    if((l.__getitem__(j+1)-l.__getitem__(j))==2):
        print(l.__getitem__(j),l.__getitem__(j+1))

l.clear()
i=0
j=0
num = eval(input("Enter from where the twin primes should start"))

for i in range(num,num+50):
    if(is_prime(i)):
        
        l.append(i)


for j in range(0,l.__len__()-1):
    if((l.__getitem__(j+1)-l.__getitem__(j))==2):
        print(l.__getitem__(j),l.__getitem__(j+1))
    
        
    
        
        

    



