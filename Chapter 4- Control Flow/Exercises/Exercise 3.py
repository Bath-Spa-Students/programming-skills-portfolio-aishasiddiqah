#Turn your if-else chain from Exercise 5-4 into an if-elifelse chain.

#•	 If the alien is green, print a message that the player earned 5 points.
#•	 If the alien is yellow, print a message that the player earned 10 points.
#•	 If the alien is red, print a message that the player earned 15 points.
#•	 Write three versions of this program, making sure each message is printed for the appropriate color alien.

color=input("The color of the alien is: ")
if color=="green":
    print("Congratulations! You have just earned 5 points for successfully shooting the alien!")
else:
    print("You have just earned 10 points! Congratulations!")