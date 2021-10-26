#this program will calculate the average of the values inputted by the user

#Stores the user inputs
user_inputs_array=[]
#repetition structure
while 1:
    #Store user inputs
    num1=float(input("Enter a number: "))
    user_inputs_array.append(num1)
    if num1==-1:
        break
     
    else :
        continue

#Display the average       
print((sum(user_inputs_array)+1)/(len(user_inputs_array)-1))