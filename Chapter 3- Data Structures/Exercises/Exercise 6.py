#You just found out that your new dinner table won’t arrive in time for the dinner, and you have space for only two guests.
#•Start with your program from Exercise 3-5. Add a new line that prints a message saying that you can invite only two people for dinner.
#•Use pop() to remove guests from your list one at a time until only two names remain in your list. Each time you pop a name from your list, print a message to that person letting them know you’re sorry you can’t invite them to dinner.
#•Print a message to each of the two people still on your list, letting them know they’re still invited.
#•Use del to remove the last two names from your list, so you have an empty list. Print your list to make sure you actually have an empty list at the end of your program.

guest_list=["Mr.Rabbit","Ms.Alice","Mr.Mad Hatter"]
invite_1= f'I would like to cordially invite {guest_list[2]} to dinner.'
invite_2= f'I would like to cordially invite {guest_list[0]} to dinner.'
invite_3=f'Dear {guest_list[1]}, I would like to cordially invite you to dinner.'
end="I sincerely hope you will be able to attend. "
regards="\nThank you."
print(invite_1 , end , regards)
print(invite_2 , end , regards)
print(invite_3 , end , regards)

#Mr.Rabbit will not be able to attend
print(f'{guest_list[0]} will not be able to attend the dinner.')

#Since Mr.Rabbit won't be able to make it to dinner, let's invite the Queen of Hearts instead.
guest_list.remove("Mr.Rabbit")
guest_list.insert(0, "Queen of Hearts")
print(guest_list)

invite_4= f'Dear {guest_list[0]}, I would like to cordially invite you to dinner.'
print(invite_1 , end , regards)
print(invite_3 , end , regards)
print(invite_4 , end , regards)

#Uh oh! The new dinner table won't arrive in time for dinner!
#I can only accommodate two people.
#Let's inform everyone first
print("I would like to inform everyone that I will only be able to accommodate two people, unfortunately.")

#Who should I uninvite? 
#The Queen of Hearts must be very busy with her duties, so I should let her know that she need not attend such an insignificant dinner. I just hope she won't get mad.
guest_list.pop(0)
print(guest_list)

#Now, let's apologize to the Queen. I reallt hope she won't get mad.
print("Dear Queen of Hearts, \nPlease accept my sincerest apologies for withdrawing your invitation. I am truly very sorry.\nI hope you have a wonderful day.")

#I should let the other two know that they are still invited
invite_5= f'Dear {guest_list[0]}, I am sending another invitation to notify you that you are still invited to the dinner.'
invite_6= f'Dear {guest_list[1]}, I am sending another invitation to notify you that you are still invited to the dinner.'
regards_1="\nMy sincere apologies for the inconvenience. Have a nice day."
print(invite_5 , end , regards_1)
print(invite_6 , end , regards_1)

#Now that everything is settled, the list is no longer useful.
#Let's empty the list
del(guest_list[1])
del(guest_list[0])
#Make sure the list is actually empty too
print(guest_list)
