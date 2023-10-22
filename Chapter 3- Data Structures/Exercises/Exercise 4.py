#If you could invite anyone, living or deceased, to dinner, who would you invite? 
#Make a list that includes at least three people you’d like to invite to dinner. 
#Then use your list to print a message to each person, inviting them to dinner.

guest_list=["Ms.Alice","Mr.Rabbit","Mr.Mad Hatter"]
invite_1= f'I would like to cordially invite {guest_list[2]} to dinner.'
invite_2= f'I would like to cordially invite {guest_list[1]} to dinner.'
invite_3=f'Dear {guest_list[0]}, I would like to cordially invite you to dinner.'
end="I sincerely hope you will be able to attend. "
regards="\nThank you."
print(invite_1 , end , regards)
print(invite_2 , end , regards)
print(invite_3 , end , regards)