#Choose a color for an alien as you did in Exercise 5-3, and write an if-else chain.

#•If the alien’s color is green, print a statement that the player just earned 5 points for shooting the alien.
#•If the alien’s color isn’t green, print a statement that the player just earned 10 points.
#•Write one version of this program that runs the if block and another that runs the else block.

color="red"
if color=="green":
    print("Congratulations! You have just earned 5 points for shooting the alien!")
else:
    print("You have just earned 10 points! Congratulations!")

color="green"
if color=="green":
    print("Congratulations! You have just earned 5 points for shooting the alien!")
else:
    print("You have just earned 10 points! Congratulations!")

#OR

color=input("The color of the alien is ")
if color=="green":
    print("Congratulations! You have just earned 5 points for shooting the alien!")
else:
    print("You have just earned 10 points! Congratulations!")