def ninth():
    input1 = int(input("Enter a number:"))
    return smallest_prime_larger_than(input1)
def smallest_prime_larger_than(n):
    while n!=0:
        x = is_prime1(n)
        if x:
            break
        else:
            n+=1
    return n
def is_prime1(number):
    for i in range(2,int(number**0.5)+1):
        if number%i==0:
            return False
    return True
ninth()