#Write an if-else statement that assigns 0 to the variable b if the variable a is less than 10.
#Otherwise, it should assign 99 to the variable b.

#take input from user and store it in a cariable called 'a'
a=int(input("Enter any number here: "))

#write an if-else statement which assigns the number 0 to a variable named 'b' if a < 10
#otherwise if a > 10, then b=99
if a < 10:
    b=0
    print(b)
else:
    b=99
    print(b)  