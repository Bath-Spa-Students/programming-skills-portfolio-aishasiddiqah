#Write a python program that takes courses marks as input and then calculates average of all the courses. 
#After calculating the average, calculate the percentage of a student using total marks. 
#Assume the total of all the courses marks is 500 or take the total marks from the user as input. 

#Ask the user for the total number of courses
courses=int(input("How many courses do you take in total?\n"))

#Ask the user for the value of total marks
total=int(input("What are the total marks in all the subjects combined?\n"))

#Take input for the courses marks that the user attained
course_marks=int(input("How much did you score in total in all the subjects?\n"))

#calculate the average
average=course_marks/courses
print("The average is:",average)

#calculate the percentage
percentage= (course_marks/total)*100
print("The percentage is:",percentage)