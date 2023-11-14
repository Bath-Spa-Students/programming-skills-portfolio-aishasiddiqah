#Write a function called make_shirt() that accepts a size and the text of a message that should be printed on the shirt. 
#The function should print a sentence summarizing the size of the shirt and the message printed on it. 
#Call the function once using positional arguments to make a shirt. 
#Call the function a second time using keyword arguments.

#define a function named make_shirt()
#the function should accept: size of the shirt and a piece of text that should be printed on the shirt.
def make_shirt(size,text):
    print("The size of the shirt should be",size+".")
    print("The text on the shirt will say\n\t"+text+"\n")

#call the function using positional arguments:
make_shirt("medium","One day...I'm gonna make the onions cry.".upper())

#call the function using keyword arguments:
make_shirt(text="Today you are You, that is truer than true. There is no one alive who is Youer than You.",size="large")