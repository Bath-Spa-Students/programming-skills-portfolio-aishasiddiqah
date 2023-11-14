#Write a function called describe_city() that accepts the name of a city and its country. 
#The function should print a simple sentence, such as Reykjavik is in Iceland. 
#Give the parameter for the country a default value.
#Call your function for three different cities, at least one of which is not in the default country.

#define a function called describe_city()
#the function should accept the name of a city and the country that the city is located in
#also give a default value to the parameter for the country
def describe_city(city,country="Italy"):
    print(city,"is a beautiful city located in",country+".")

#call the function for three different cities
#at least one of the city should not be located in the default country
#(for this,change the value of the parameter from default to the country that the city is actually in)

#for the cities that are within the default country:
describe_city("Venice")
describe_city("Milan")

#for the city that is not within the default country:
describe_city(city="Amsterdam",country="Netherlands")