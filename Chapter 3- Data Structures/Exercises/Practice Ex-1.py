#Given a Python list, write a program to remove all occurrences of item 20.

#Given list:
#list1 = [5, 20, 15, 20, 25, 50, 20]

#using for loop:
list1 = [5, 20, 15, 20, 25, 50, 20]
for num in list1:
    if num==20:
        list1.remove(num)
print(list1)

#OR
#using the pop() function:
list1 = [5, 20, 15, 20, 25, 50, 20]
list1.pop(6)
list1.pop(3)
list1.pop(1)
print(list1)

#OR
#using the remove() function:
list1 = [5, 20, 15, 20, 25, 50, 20]
list1.remove(20)
list1.remove(20)
list1.remove(20)
print(list1)