#Write a loop that prompts the user to enter a series of pizza toppings until they enter a 'quit' value. 
#As they enter each topping, print a message saying you’ll add that topping to their pizza.

topping = "What toppings would you like to add on your pizza?\n"
print(topping)
while topping != "quit":
  topping = input ("\n"+topping + " will be added to your pizza. \nWhat other topping would you like on your pizza?\n")
print("Thank you! Please wait while we get your order ready.")

 
#password = "SecretWord"
#guess = input()
#while guess != password:  
  #guess = input() 
#print("Access Granted") 