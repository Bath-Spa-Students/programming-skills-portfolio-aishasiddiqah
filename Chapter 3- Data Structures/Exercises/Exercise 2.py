#Start with the list you used in Exercise 1, but instead of just
#printing each person’s name, print a message to them. 
#The text of each message should be the same, but each message should be personalized with the person’s name.

names= ["Esha","Fatima","Laraib","Mehreen","Sundas","Zahra"]
print("Have a great day", names[0] + ".")
print("Have a great day", names[1] + ".")
print("Have a great day", names[2] + ".")
print("Have a great day", names[3] + ".")
print("Have a great day", names[4] + ".")
print("Have a great day", names[5] + ".")
#OR
msg="Have a great day"
end="!"
print(msg,names[0],end)
print(msg,names[1],end)
print(msg,names[2],end)
print(msg,names[3],end)
print(msg,names[4],end)
print(msg,names[5],end)