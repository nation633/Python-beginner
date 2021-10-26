#This program shows the multiplication table of the number the user enters

#Stores the users input
user_input=int(input("Enter an integer: "))

for i in range(0,11):
    print(str(user_input) + "*" + str(i) + "=" + str(user_input*i))
    
