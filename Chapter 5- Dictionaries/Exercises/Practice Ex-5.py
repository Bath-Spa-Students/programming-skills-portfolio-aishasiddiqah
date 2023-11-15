#Write a Python program to merge two dictionaries into one.

myself = {"Name":"Aisha",
      "Age: ":"18",
      "Siblings: ":"2 siblings",
      "Country_of_Residence: ":"United Arab Emirates",
      "City: ":"Ajman",
      "Nationality: ":"Pakistan"}

favorites={"fruit: ":"mango",
      "vegetable":"tomato",
      "fast_food":"pizza",
      "snacks":"chips",
      "dessert":"tiramisu",}

print(myself|favorites)
#OR
print({**myself,**favorites})