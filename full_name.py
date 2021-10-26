#This program will be used to validate that a user enters inputs atleast two names when asked to enter their full name

#store the users full name
full_name=input("Enter your full name: ")

if len(full_name)==0:
    print ("Enter your fullname: ")
    
elif len(full_name) < 4:
        print ("Please make sure that you have entered your name and surname")
        
elif len(full_name) > 25:
    print ("Please make sure that you have entered your full name")

else:
    print ("Thank you for writing your name!")
    