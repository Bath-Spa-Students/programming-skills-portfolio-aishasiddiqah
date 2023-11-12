#Make a dictionary containing three major rivers and the country each river runs through. 
#One key-value pair might be 'nile': 'egypt'.

#* Use a loop to print a sentence about each river, such as The Nile runs through Egypt.
#* Use a loop to print the name of each river included in the dictionary.
#* Use a loop to print the name of each country included in the dictionary.

#3 major rivers and the country each river runs through
major_rivers = {'Euphrates':'Turkey',
          'Rhine':'Switzerland',
          'Nile':'Egypt'}

#loop to print a sentence about each river
for river, country in major_rivers.items():
    print("The",river,"River", "runs through",country+".","\n")

#loop to print the name of each river in the dictionary major_rivers:
print("The rivers included within the dictionary are:" )
for river in major_rivers.keys():
    print(river, "River")

#loop to print the name of each country included in the dictionary:
print("\nThe following countries are included within the dictionary:")
for country in major_rivers.values():
    print(country)