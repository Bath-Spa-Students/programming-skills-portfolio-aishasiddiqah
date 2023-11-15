#You have been given a Python list. Write a program to find value 20 in the list, and if it is present,
#replace it with 200. 
#Only update the first occurrence of an item. 
#Work with the given list:
#list1 = [5, 10, 15, 20, 25, 50, 20]

#copy the list
list1 = [5, 10, 15, 20, 25, 50, 20]

#find the value 20 in the list
#if present, replace with 200
x=list1.index(20)
print(x)

#the value 20 is present at the index 3
list1.insert(3,200)
print(list1)

#OR alternatively, replace the index value with the variable assigned to find the index #
# (in this case, the value is x)
list1.insert(x,200)
print(list1)
