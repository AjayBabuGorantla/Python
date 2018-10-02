def polite_num(x):
    for a in range(1,x):
        for n in range(2,x):
            num = (n/2)*(2*a + (n-1))
            if(num ==x):
                term =a
                
                for i in range(0,n):
                    
                    print(term,end=" ")
                    
                    term = term+1
                print("\n")
    else:
        print("impolite number")
        
        
num = eval(input("Enter the number :"))
polite_num(num)