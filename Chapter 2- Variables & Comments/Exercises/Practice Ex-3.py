#Write a python program that takes an input 5 from user and then type cast those values to string, int
# and float in the separate variables. 
#Print all the variables.

#take input from user
info=input("Type a value: ")

#typecast the value that was taken from the user into: string, integer and float
#string
str_1=str(info)
#integer
int_1=int(float(info))
#float
float_1=float(info)

#print all the variables
print("\nString:")
print(str_1)
print("\nInteger:")
print(int_1)
print("\nFloat:")
print(float_1)