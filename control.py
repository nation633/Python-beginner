#This program is going to expand on the first control structure task we created

#Gets and Stores the age of the user
age= int(input("Enter your age: "))

#checks id user is older than 18 years old

if age >= 18:
    print("You are old enough!")
    
elif age>16 and age<18:
    print("Almost there")
    
else:
    print("You're just too young")
