#Modify the make_shirt() function so that shirts are large by default with a message that reads I love Python. 
#Make a large shirt and a medium shirt with the default message, and a shirt of any size with a different message.

#define the make_shirt() function
#this time, the size will be large by default and the message will read 'I love Pythin'
def make_shirt(size="large",printed_text="I love Python"):
    print("The size of the shirt should be",size+".")
    print("The text on the shirt will say:\n\t"+printed_text+"\n")

#make a large and medium shirt with the default message 
#for the large sized shirt, simply call the function
make_shirt()

#for a medium shirt, use the size keyword to change from the default size to size of your choice
#the printed piece of text message will remain the same 
make_shirt(size="medium")

#make a  shirt of any size, this time with a different message printed on it
make_shirt(size="extra large",printed_text="If we wait until we are ready, we will be waiting for the rest of our lives.")