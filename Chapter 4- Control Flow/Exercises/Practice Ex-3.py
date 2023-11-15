#Write a python program with nested decision structures that perform the following: 
#If amount1 is greater than 10 and amount2 is less than 100, display the greater of amount1 and amount2

#Take user input for assigning values to variables 'amount1' and 'amount2'
amount1=int(input("Enter a value here: "))
amount2=int(input("Enter a value here: "))
print("amount1=",amount1)
print("amount2=",amount2)

#for the nested decision structure:
#amount1 > 10 and amount2 < 100, then compare the two
if amount1 > 10 and amount2 < 100:
    if amount1 < amount2:
        print("amount2 is the greater value")
    elif amount1 > amount2:
        print("amount1 is the greater value")
else:
    print("The values provided are invalid.")