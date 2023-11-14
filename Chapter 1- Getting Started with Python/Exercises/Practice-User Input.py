#Create a personal identification profile with user input

name=(input("Enter your name:"))
age=int(input("Enter your age:"))
number=int(input("Enter your contact number:"))
father=(input("Enter your father's name:"))
mother=(input("Enter your mother's name:"))
address=(input("Enter your address:"))
siblings=int(input("Enter the number of siblings you have:"))
food=(input("Enter your favourite food:"))
drink=(input("Enter your favourite drink:"))
hobby=(input("Enter your favourite hobby:"))

#print all of the above 
print("\nMy name is",name+".")
print("I am",age,"years old.")
print("My contact number is",number,".")
print("My father's name is",father+".")
print("My mother's name is",mother+".")
print("My address is",address+".")
print("I have",siblings,"siblings.")
print("My favorite food is",food+".")
print("My favorite drink is",drink+".")
print("My hobbies include",hobby+".")