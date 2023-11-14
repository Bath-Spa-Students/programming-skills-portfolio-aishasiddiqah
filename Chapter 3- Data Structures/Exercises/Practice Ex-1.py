#Given a Python list, write a program to remove all occurrences of item 20.

#Given list:
list1 = [5, 20, 15, 20, 25, 50, 20]
list1.pop(6)
list1.pop(3)
list1.pop(1)
print(list1)

#OR
list1 = [5, 20, 15, 20, 25, 50, 20]
list1.remove(20)
list1.remove(20)
list1.remove(20)
print(list1)

#OR
list1 = [5, 20, 15, 20, 25, 50, 20]
(f'{list1.remove(20)}{list1.remove(20)}{list1.remove(20)}')
print(list1)

#OR
list1 = [5, 20, 15, 20, 25, 50, 20]
(f'{list1.pop(6)}{list1.pop(3)}{list1.pop(1)}')
print(list1)

#OR
list1 = [5, 20, 15, 20, 25, 50, 20]
while True:
    list1.remove(20)
    if list1!=20
    break


