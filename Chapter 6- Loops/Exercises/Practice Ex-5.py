#Write a Python program that uses a while loop to find the largest number among a series of
#user-input values until they enter '0' to exit the loop.

largest_num= None

while True:
    value=int(input("Enter your number here: "))
    if value==0:
        break

    value=int(value)
    if largest_num is None or value>largest_num:
        largest_num=value

print("The largest number is:",largest_num)


