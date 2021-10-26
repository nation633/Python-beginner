#This program verifies if a password is suitable or not

have_length= False
up_case= False
low_case= False
have_num=False

#Stores the users input.
pass_length=bool(input("Does your password have more than 6 characters (Enter yes or just hit the enter key): "))
pass_up_case=bool(input("Does your password have an upper case character (Enter yes or just hit the enter key): "))
pass_low_case=bool(input("Does your password have lower case characters (Enter yes or just hit the enter key): "))
pass_have_num=bool(input("Does your password have number characters (Enter yes or just hit the enter key): "))

bool_sum = (pass_length + pass_up_case + pass_low_case + pass_have_num)


if bool_sum>=3:
    print("This is a valid Password!!")

else:
    print("This is not a valid Password!!")