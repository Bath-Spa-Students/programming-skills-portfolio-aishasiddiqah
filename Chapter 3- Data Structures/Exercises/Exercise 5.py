#You just heard that one of your guests can’t make the dinner, so you need to send out a new set of invitations. 
#You’ll have to think of someone else to invite.

#•Start with your program from Exercise 3-4. Add a print() call at the end of your program stating the name of the guest who can’t make it.
#•Modify your list, replacing the name of the guest who can’t make it with the name of the new person you are inviting.
#•Print a second set of invitation messages, one for each person who is still in your list.

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
