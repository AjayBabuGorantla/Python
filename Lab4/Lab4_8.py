def eighth():
    input1 = int(input("Enter a number:"))
    return prime_count(input1)
def prime_count(n):
    count=0
    for i in range(2,n):
        x = is_prime(i)
        if x:
            count+=1
        else:
            continue
    return count
def is_prime(number):
    for i in range(2,int(number**0.5)+1):
        if number%i==0:
            return False
    return True
eighth()