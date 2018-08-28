import math

for number in range(100,1000):
    first_digit= int(number/100)
    second_digit= int((number%100)/10)
    third_digit= int((number%100)%10)
    sum_of_cubes_of_digits = pow(first_digit,3)+pow(second_digit,3)+pow(third_digit,3)
    if(sum_of_cubes_of_digits==number):
        print(number)
