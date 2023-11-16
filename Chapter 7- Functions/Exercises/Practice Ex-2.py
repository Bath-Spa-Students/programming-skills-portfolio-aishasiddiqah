#Write a Python function that calculates the factorial of a given positive integer using recursion.

#define a function named factorial
#the function should calculate the factorial of a given positive integer using recursion
def factorial(n):
    if n==1:
        return n
    else:
        return (n*factorial(n-1))

integer=1

#since the integer has to be positive
#check and confirm in case the number is negative
if integer<0:
    print("The factorial can only be calculated for positive numbers, not negative numbers.")
elif integer==0:
    print("The factorial of 0 is 1.")
else:
    print("The factorial of",integer,"is:\n",factorial(integer))