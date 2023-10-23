#Stripping names
#Use a variable to represent a person’s name, and include some whitespace characters at the beginning and end of the name. 
#Make sure you use each character combination, “\t” and “\n”, at least once.
#Print the name once, so the whitespace around the name is displayed. 
#Then print the name using each of the three stripping functions, lstrip(), rstrip(), and strip().

name = "\tAisha\t\n"
print (name)
print("My name is", name , ".")

#Using the lstrip() method:
print("My name is", name.lstrip() , ".")

#Using the rstrip() method:
print("My name is", name.rstrip() , ".")

#Using the strip() method:
print("My name is", name.strip() , ".")
