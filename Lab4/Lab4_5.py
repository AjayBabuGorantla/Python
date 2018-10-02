def fifth():
    input1 = int(input("Enter a number:"))
    return sum_of_digits(input1)
def sum_of_digits(n):
    sum1=0
    while n>0:
        sum1+= n%10
        n=n//10
    return sum1
print(fifth())
