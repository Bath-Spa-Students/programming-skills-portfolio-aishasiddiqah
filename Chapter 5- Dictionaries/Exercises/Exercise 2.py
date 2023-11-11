#A Python dictionary can be used to model an actual dictionary. 
#However, to avoid confusion, let’s call it a glossary.

#* Think of five programming words you’ve learned about in the previous chapters. 
#Use these words as the keys in your glossary, and store their meanings as values.

#* Print each word and its meaning as neatly formatted output. 
#You might print the word followed by a colon and then its meaning, or print the word on one line and then print its meaning indented on a second line. 
#Use the newline character (\n) to insert a blank line between each word-meaning pair in your output.

glossary = {'variable' : 'a quantity used to store data',
            'float' : 'a number that contains a decimal point',
            'integer' : 'a number that does not contain a decimal point',
            'input' : 'a function where a user enters data',
            'tuple' : 'a data type which is similar to lists, but is immutable'
            }
print("variable:"+"\n",glossary['variable'])
print("\n""float:"+"\n",glossary['float'])
print("\n""integer:"+"\n",glossary['integer'])
print("\n""input:"+"\n",glossary['input'])
print("\n""tuple:"+"\n",glossary['tuple'])


