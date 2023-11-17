#Make several dictionaries, where each dictionary represents a different pet. 
#In each dictionary, include the kind of animal and the owner’s name. 
#Store these dictionaries in a list called pets. 
#Next, loop through your list and as you do, print everything you know about each pet.

#pet dictionaries
#for pet_1:
pet_1 = {'Name of pet':' Fluffy',
         'Name of owner':' Fatima',
         'Kind of animal':' Cat',
         'Age of the pet':' 3 years',
         'Colour of the pet':' White',
         'Any specific allergies':' None'}

#for pet_2:
pet_2 = {'Name of pet':' Cookie',
         'Name of owner':' Sundas',
         'Kind of animal':' Cat',
         'Age of the pet':' 4 years',
         'Colour of the pet':' Brown',
         'Any specific allergies':' None'}

#for pet_3:
pet_3 = {'Name of pet':' Lucky',
         'Name of owner':' Anosha',
         'Kind of animal':' Dog',
         'Age of the pet':' 2 years',
         'Colour of the pet':' White, with a few black spots',
         'Any specific allergies':' Beef'}

#for pet_4:
pet_4 = {'Name of pet':' Goldilocks',
         'Name of owner':' Maheen',
         'Kind of animal':' Fish',
         'Age of the pet':' 2 years',
         'Colour of the pet':' Red',
         'Any specific allergies':' None'}

#make a list called 'pets' and store all the pet dictionaries in that list
pets = [pet_1,pet_2,pet_3,pet_4]

#loop through the list and print all the information about each pet
for pet in pets:
    print ("\nThe following information is available regarding the pet"+pet['Name of pet'].title()+":")
    for section, information in pet.items():
        print(f'{section}:{information}')