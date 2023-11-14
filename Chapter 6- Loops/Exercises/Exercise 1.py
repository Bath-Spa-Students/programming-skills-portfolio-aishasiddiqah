#Write a loop that prompts the user to enter a series of pizza toppings until they enter a 'quit' value. 
#As they enter each topping, print a message saying you’ll add that topping to their pizza.

#loop that prompts user to enter their desired pizza toppings (loop continues until user enters 'quit'):
question = "What toppings would you like to add on your pizza?\n"
while topping != "quit":
  topping = input (question)
  if topping != "quit":
    print("\t",topping.capitalize(),"will be added to your pizza.\n")
  if topping == "quit":
    break
print("\tThank you! Please wait while your order is being prepared.")