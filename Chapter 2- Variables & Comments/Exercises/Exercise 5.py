#A girl heads to a computer shop to buy some USB sticks. 
#She loves USB sticks and wants as many as she can get for £50. They are £6 each.
#Write a programme that calculates how many USB sticks she can buy and how many pounds she will have left.
#You will to use the arithmetic operators to complete this exercise.

#Assign values to variables
x = 50
y = 6

#if £6 = 1 USB
#then £50 = ? USB sticks

#for number of USB sticks the girl can buy:
a=int(x/y)
print("The girl can buy", a, "USB sticks with £50.")

#amount of money the girl will have left:
b=y*a
c=x-b
print(f'She will have {c} pounds left after buying {a} USB sticks.')