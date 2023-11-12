#Now that you know how to loop through a dictionary, clean up the code from Exercise 6-3 (page 99) by replacing your series of print()
#calls with a loop that runs through the dictionary’s keys and values. 
#When you’re sure that your loop works, add five more Python terms to your glossary.
#When you run your program again, these new words and meanings should automatically be included in the output.

glossary = {'variable' : 'a quantity used to store data',
            'index' : 'the numerical value used to detect the position of an object within a list, tuple or even a string',
            'integer' : 'a number that does not contain a decimal point',
            'input' : 'a function where the user is required to enter data',
            'tuple' : 'a data type which is similar to lists and stores multiple data values, but is immutable',
            'list' : '',
            'loop' : '',
            'float' : 'a number containing a decimal',
            'sorted' : '',
            'reverse' : ''
            }

# print the words and their meanings
for word, definition in glossary.items():
    print(word + ":" + "\n" + definition + "\n")
