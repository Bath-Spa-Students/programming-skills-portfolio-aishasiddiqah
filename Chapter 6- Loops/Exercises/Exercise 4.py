#Make a list called sandwich_orders and fill it with the names of various sandwiches. 
#Then make an empty list called finished_sandwiches.
#Loop through the list of sandwich orders and print a message for each order, such as I made your tuna sandwich. 
#As each sandwich is made, move it to the list of finished sandwiches. 
#After all the sandwiches have been made, print a message listing each sandwich that was made.

#list of sandwich names
sandwich_orders=["chicken sandwich","egg sandwich","grilled cheese sandwich","fajita sandwich"]
#empty list for finished sandwiches
finished_sandwiches=[]

#loop through the order list + print a message for each order in the list
while sandwich_orders:
    sandwich=sandwich_orders.pop()
    print("Your",sandwich,"is ready. Enjoy!")
    finished_sandwiches.append(sandwich)

#print a message listing each sandwich that was made
for sandwich in finished_sandwiches:
    print("\tThe",sandwich,"was prepared.")
