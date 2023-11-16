#Write a Python program that defines a function to check whether a given number is prime.

#by using the math module
import math

#define a function called prime_num()
def prime_num(z):
    if z<=1:
        return False
    for x in range(2, int(math.sqrt(z))+1):
        if z%x==0:
            return False
    return True

#ask the user to input a value
z=int(input("Enter a number: "))
print(prime_num(z))