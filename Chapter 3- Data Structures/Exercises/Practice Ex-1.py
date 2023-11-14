#Given a Python list, write a program to remove all occurrences of item 20.

#Given list:
list1 = [5, 20, 15, 20, 25, 50, 20]
for num in list1:
    if num==20:
        list1.remove(num)
print(list1)

