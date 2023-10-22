#Think of at least five places in the world you’d like to visit.
#•	 Store the locations in a list. Make sure the list is not in alphabetical order.
#•	 Print your list in its original order. Don’t worry about printing the list neatly,just print it as a raw Python list.
#•	 Use sorted() to print your list in alphabetical order without modifying the actual list.
#•	 Show that your list is still in its original order by printing it.
#•	 Use sorted() to print your list in reverse alphabetical order without changing the order of the original list.
#•	 Show that your list is still in its original order by printing it again.
#•	 Use reverse() to change the order of your list. Print the list to show that its order has changed.
#•	 Use reverse() to change the order of your list again. Print the list to show it’s back to its original order.
#•	 Use sort() to change your list so it’s stored in alphabetical order. Print the list to show that its order has been changed.
#•	 Use sort() to change your list so it’s stored in reverse alphabetical order. Print the list to show that its order has changed.

places=["Venice","Florence","Geneva","Amsterdam","Manchester"]
print(places)

#in alphabetical order
print("Alphabetical order (Temporary):")
print(sorted(places))

#prove that the list is not permanently changed
print("Original format:")
print(places)

#for reverse alphabetical order
print("Reverse alphabetical order (Temporary):")
print(sorted(places, reverse=True))

#prove that list remains unchanged
print("Original format:")
print(places)

#reverse the elements of the list
print("Reverse order:")
places.reverse()
print(places)

#reverse the list again to its original order
print("Original format (after reversing):")
places.reverse()
print(places)

#alphabetical order, but this time it should be permanent
print("Alphabetical order (Permanent):")
places.sort()
print(places)

#reverse alphabetical order, but also permanent
print("Reverse alphabetical order (Permanent):")
places.sort(reverse=True)
print(places)