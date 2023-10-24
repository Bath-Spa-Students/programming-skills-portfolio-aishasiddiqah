#Imagine an alien was just shot down in a game. 
#Create a variable called alien_color and assign it a value of 'green', 'yellow', or 'red'.

#•Write an if statement to test whether the alien’s color is green. If it is, print a message that the player just earned 5 points.
#•Write one version of this program that passes the if test and another that fails. (The version that fails will have no output.)

alien_color="yellow"
if alien_color=="green" :
    print("That is correct! You have just earned yourself five extra points!")

alien_color="green"
if alien_color=="green" :
    print("That is correct! You have just earned yourself five extra points!")

#OR
#just let the user enter the color directly

alien_color=input("What is the color of the alien?")
if alien_color == "green" :
    print("You are correct! The color of the alien is green. You have just earned 5 points.")
else:
    print("That is incorrect! The colour of the alien is green, not" , alien_color +".")