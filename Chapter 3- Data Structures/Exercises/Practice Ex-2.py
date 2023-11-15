#Write a statement that creates a list with the following strings: 
#'Einstein', Newton' , 'Copernicus', and 'Kepler'

#assign the strings to variables
str_1="Einstein"
str_2="Newton"
str_3="Copernicus"
str_4="Kepler"

#make an empty list
list_1=[]

#add the strings to the list
#for adding multiple strings, the extend() method can be used
list_1.extend([str_1,str_2,str_3,str_4])
print(list_1)

#OR
#the append() method may be used, however it only appends one value
list_2=[]

list_2.append(str_1)
list_2.append(str_2)
list_2.append(str_3)
list_2.append(str_4)
print(list_2)