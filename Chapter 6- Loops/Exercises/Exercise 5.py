#Using the list sandwich_orders from Exercise 7-8, make sure the sandwich 'pastrami' appears in the list at least three times. 
#Add code near the beginning of your program to print a message saying the deli has run out of pastrami, 
#and then use a while loop to remove all occurrences of 'pastrami' from sandwich_orders. 
#Make sure no pastrami sandwiches end up in finished_sandwiches.

#add pastrami sandwich to the list made in the previous execise 
sandwich_orders=["chicken sandwich","pastrami sandwich","egg sandwich","grilled cheese sandwich","pastrami sandwich","fajita sandwich","pastrami sandwich"]
finished_sandwiches=[] 

#print a message saying that the deli ran out of pasrami sandwiches
print("We have run out of pastrami sandwiches today. Our apologies for any inconvinience caused. \nThank you for your understanding.\n")

#use a while loop to remove all pastrami sandwiches from list
while 'pastrami sandwich' in sandwich_orders:
    sandwich_orders.remove("pastrami sandwich")

#loop through the order list and print a message for each order that is prepared
while sandwich_orders:
    sandwich=sandwich_orders.pop()
    print("Your",sandwich,"is ready. Enjoy!")
    finished_sandwiches.append(sandwich)

#print a message listing each sandwich that was made
for sandwich in finished_sandwiches:
    print("\tThe",sandwich,"was prepared.")

