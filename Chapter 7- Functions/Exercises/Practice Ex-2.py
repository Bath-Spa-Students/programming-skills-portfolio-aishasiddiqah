#Write a Python function that calculates the factorial of a given positive integer using recursion.

#define a function named factorial
#the function should calculate the factorial of a given positive integer using recursion
def factorial(n):
    if n==0 or n==1:
        return n
    else:
        return (n*factorial(n-1))

#take user input to obtain the integer
integer=(input("Enter an integer here: "))

#since the integer has to be positive
#check and confirm in case the number is negative


print("The factorial of",integer,"is:\n",factorial(integer))