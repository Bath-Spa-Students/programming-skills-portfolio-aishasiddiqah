#Compute the area of triangle.
#The three sides of a triangle are a, b and c
#The measurements of the three sides of the triangle are:
a=float(input('Enter first side:'))
b=float(input('Enter second side:'))
c=float(input('Enter third side:'))

#Calculate the semi-perimeter of the triangle:
#Formula for semi-perimeter of a triangle is
s=(a+b+c)/2

#Calculate the area of triangle:
#Formula for finding area of triangle
area=(s*(s-a)*(s-b)*(s-c))**0.5
print(area)

#Calculate the area of the triangle
#Enter the values for the three sides when the program is running
