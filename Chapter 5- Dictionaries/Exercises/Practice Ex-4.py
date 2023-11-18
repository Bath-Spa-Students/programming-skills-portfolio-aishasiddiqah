#Write a Python program to iterate through both the keys and values of a dictionary and print them.

desserts = {"Tiramisu":"Italy",
      "Cheesecake":"Greece",
      "Pavlova":"Australia",
      "Mochi":"Japan",
      "Scones":"Scotland"}

#to iterate through both keys and values
for key,value in desserts.items():
    print(key,value)