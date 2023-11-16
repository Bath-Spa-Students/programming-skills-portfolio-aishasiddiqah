#Write a Python program that uses a function to check if a given number is prime or not.

#take user input 
num=int(input("Enter a number of your choice: "))

#by using the range() function
if num>1:
    for x in range(2,num):
        if(num%x)==0:
            print("The number",num,"is NOT a prime number.")
            break
    else:
        print("The number",num,"is a prime number.")
else:
    print("The number",num,"is NOT a prime number.")