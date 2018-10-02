def sixth():
    input1 = int(input("Enter a number:"))
    return largest_fibo(input1)
def largest_fibo(n):
    a,b=0,1
    while b<n :
        a,b=b,a+b
        if(b>n):
            return a
sixth()