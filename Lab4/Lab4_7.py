def seventh():
    input1 = int(input("Enter a number:"))
    return prime_factors(input1)
def prime_factors(n):
    numbers=[]
    while n%2==0:
        numbers.append(2)
        n=n//2
    for i in range(3,int(n**0.5)+1,2):
        while n%i==0:
            numbers.append(i)
            n = n//i
    if n > 1:
        numbers.append(n)
    return numbers
print(seventh())