def a():
    m = int(input("Enter a number:"))
    n = int(input("Enter another number:"))
    print(multiply(m,n))
def multiply(m,n):
    if n==0:
        return 0
    else:
        return (multiply(m,n-1) + m)
a()

def b():
    x = int(input("Enter a number:"))
    y = int(input("Enter another number:"))
    print(power(x,y))
def power(x,y):
    if y==0:
        return 1
    else:
        return (power(x,y-1)*x)
b()

def c():
    input1 = str(input("Enter a number:"))
    print(palindrome(input1))
def palindrome(s):
    if len(s) < 1:
        return "Palindrome"
    else:
        if s[0] == s[-1]:
            return palindrome(s[1:-1])
        else:
            return "Not Plaindrome"
c()

def d():
    input1=int(input("Enter a number:"))
    input2=int(input("Enter another number:"))
    print(gcd(input1,input2))
def gcd(a,b):
    r=a%b
    if r==0:
        return b
    if r==1:
        return 1
    return gcd(b,r)
d()

def e():
    input1 = int(input("Enter a number:"))
    return sum_of_digits1(input1)
def sum_of_digits1(x):
    a=x%10
    if x==0:
        return 0
    x=x//10
    return sum_of_digits1(x)+a
print(e())

def f():
    input1 = int(input("Enter a positive number:"))
    return (dec2bin(input1))
def dec2bin(n):
    if n == 0:
        return '0'
    else:
        return dec2bin(n//2) + str(n%2)
print(f())
