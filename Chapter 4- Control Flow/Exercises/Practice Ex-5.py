#Write a Python program that uses the elif statement to determine the season based on the
#month provided as input.

#take user input
month=str(input("Please enter the month: "))

#for determining the season based on the month:
# summer= june, july, august  
# autumn= september, october, november
# winter= december, january, february
# spring= march, april, may

if month=="september" or month=="october" or month=="november":
    season="autumn"
    print("It is the",season,"season.")
elif month=="december" or month=="january" or month=="february":
    season="winter"
    print("It is the",season,"season.")
elif month=="march" or month=="april" or month=="may":
    season="spring"
    print("It is the",season,"season.")
elif month=="june" or month=="july" or month=="august":
    season="summer"
    print("It is the",season,"season.")