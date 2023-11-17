#Write a loop that never ends, and run it. 
#(To end the loop, press ctrl-C or close the window displaying the output.)

never_ending=input("The weather is very nice today, isn't it?\n")
while True:
    print(never_ending)
    if never_ending=="yes":
            print("Yes, the weather is quite pleasant.")