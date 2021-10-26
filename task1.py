#	his program will compare three values stored in variables and display the lager value,determine if the numbers are odd or even and sort the values in descending order

#Stores number values
num1=45
num2=125
num3=8

#Compares two values and determines which one is greater
if num1>num2:
    print (str(num1) + " " + "is the greater value")
elif num2>num1:
    print (str(num2) + " " + "is the greater value")
else:
    print ("The vallues are equal")
    
if num1 % 2 == 0:
        print(num1, "is EVEN")
else:
        print(num1, "is ODD")

#Determines if the values are even or odd numbers!    
if num2 % 2 == 0:
    print(num2, "is EVEN")
        
else:
    print(num2, "is ODD")
    
if num3 % 2 == 0:
    print(num3, "is EVEN")
                 
else:
    print(num3, "is ODD")
        
#Sorts the values in ascending order        
list1=(num1,num2,num3)
list1 = sorted(list1, key=int)

print (list1)

