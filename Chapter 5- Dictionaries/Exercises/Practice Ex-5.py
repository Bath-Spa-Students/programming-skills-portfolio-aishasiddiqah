#Write a Python program to merge two dictionaries into one.

desserts = {"Tiramisu":"Italy",
      "Cheesecake":"Greece",
      "Pavlova":"Australia",
      "Mochi":"Japan",
      "Scones":"Scotland"}

food={"fruit: ":"mango",
      "vegetable":"tomato",
      "fast_food":"pizza",
      "snacks":"chips"}

print(desserts|food)
#OR
print({**desserts,**food})