#Assume the lists numbers_1 has 100 elements and numbers_2 is an empty list. 
#Write code that copies the values in numbers to numbers_2.

#assume a list called numbers1 has 100 elements
numbers_1=["Hi"]*100
print(numbers_1)

#assume numbers2 is an empty list
numbers_2=[]

#copy the values in numbers1 to numbers2
numbers_2=numbers_1[0:100]
print(numbers_2)

#can also use [:] instead of [0:100]-both give the same result
#to check number of elements in the lists
print(len(numbers_1))
print(len(numbers_2))