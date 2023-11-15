#Write a Python program that uses the elif statement to determine the season based on the
#month provided as input.

#take user input
month=input("Please enter the month: ")

#for determining the season based on the month:
# summer= june, july, august  
# autumn= september, october, november
# winter= december, january, february
# spring= march, april, may

if month=="june" or "july" or "august":
    season="summer"
    print("It is the",season,"season.")
elif month=="september" or "october" or "november":
    season="autumn"
    print("It is the",season,"season.")
elif month=="december" or "january" or "february":
    season="winter"
    print("It is the",season,"season.")
elif month=="march" or "april" or "may":
    season="spring"
    print("It is the",season,"season.")