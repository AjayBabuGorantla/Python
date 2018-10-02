def fourth():
    input1 = int(input("Enter a number:"))
    return square_sum_to(input1)
def square_sum_to(n):
    return (n*(n+1)*(2*n + 1))//6
print(fourth())
