#A movie theater charges different ticket prices depending on a person’s age. 
#If a person is under the age of 3, the ticket is free; 
#if they are between 3 and 12, the ticket is $10; and if they are over age 12, the ticket is $15. 
#Write a loop in which you ask users their age, and then tell them the cost of their movie.

#make a loop asking the user's age and tell them the cost of the tickets accordingly.
while True:
    age=input("Please enter your age: ")
    if age=="quit":
        break

    age=int(age) 
    #this is separate because pof the (int) function(if used overall, the 'quit' value is not recognized)
    if age<3: 
        print("You don't have to pay! Your ticket is free!\n\tEnjoy!")
    elif age==3 or age<=12:
        print("The cost of your ticket is: $10.\n\tEnjoy!")
    else:
        print("The cost of you ticket is: $15.\n\tEnjoy!")
end=("\tThank you!")
print(end.upper())