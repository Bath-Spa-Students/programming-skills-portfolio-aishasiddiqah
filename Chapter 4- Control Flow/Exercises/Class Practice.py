#if statement
drinks = int(input("Amount of drinks ordered:"))
tip=0
if drinks > 50 :
    tip=20
else:
    tip=5
print("Amount given in tips:" , str(tip))

#comparing strings (using ascii)
str1="mary"
str2="mark"
str1>str2
print("str1 is greater than str2")

#every if has an else#

#nested decision structure
#for a job at a restaurant #food comp.
previous_exp=(input("Do you have any previous work experience within this field?"))
if previous_exp>"yes":
        print("You may proceed")
else :
        print("You need to have previous work experience to be able to apply")   

#skills in the kitchen in terms of cooking 
savory=(input("Do you know how to make savory food?"))
sweet=(input("Do you know how to make sweet food/desserts?"))
if savory-"yes" and sweet-"yes":
        print("Please make sure you go through the rules and regulations before applying. Thank you.")
else :
      print("You are not eligible to apply.")



