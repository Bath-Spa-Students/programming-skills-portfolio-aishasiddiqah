#Write a Python program to iterate through both the keys and values of a dictionary and print them.

myself = {"Name":"Aisha",
      "Age: ":"18",
      "Siblings: ":"2 siblings",
      "Country_of_Residence: ":"United Arab Emirates",
      "City: ":"Ajman",
      "Nationality: ":"Pakistan"}

#to iterate through both keys and values
for key,value in myself.items():
    print(key,value)