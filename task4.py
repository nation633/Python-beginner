#This program will ask the user to enter an integer and determine if it is divisible by 2 and 5, divisible by 2 or 5, not divisible by 2 or 5

#store the integer the user inputs
users_int= int(input("Enter an integer: "))


if users_int % 2==0:
    print (str(users_int) + " " + "is divisible by 2")

elif users_int % 5 ==0:
    print (str(users_int) + " " + "is divisible by 5")
    
else:
    print (str(users_int) + " " + "is not divisible by both 2 and 5 ")
    

if users_int % 2==0 or users_int % 5==0:
    print (str(users_int) + " " + "is divisible")
    
else:
    print (str(users_int) + " " + "is not divisible by both 2 and 5 ")
    
if users_int % 2 !=0:
    print (str(users_int) + " " + "is not divisible by  2")
  
elif users_int % 5 !=0: 
    print (str(users_int) + " " + "is not divisible by 5")
     
else:
    print (str(users_int) + " " + "can be divided by both 2 and 5 ")
    
    