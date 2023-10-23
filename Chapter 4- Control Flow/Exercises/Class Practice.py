#if statement
drinks = int(input("Amount of drinks ordered:"))
tip=0
if drinks > 50 :
    tip=20
else:
    tip=5
print("Amount given in tips:" , str(tip))

