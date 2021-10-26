#This program allows the user to access two different financial calculators.

import math

#stores the users choice
users_options= input("Choose either 'Investment' or 'bond' from the menu below .\n \ninvestment  - to calculate the amount of interest you'll earn on interest \nbond        - to calculate the amount you'll have to pay on a home loan \nEnter your choice: ")


if users_options=="INVESTMENT" or users_options=="investment":
    
    #Store users inputs
    deposit_amount=float(input("Enter the smount you'd like to deposit: "))
    interest_rate=float(input("Enter your interest rate in percentege, don't use the percentage sign just enter the number: " ))/100
    number_of_years=int(input("Enter the duration of your investment in years: "))
    type_of_interest=input("Do wont compound or simple interest?: ")
    if type_of_interest=="COMPOUND" or type_of_interest=="compound":
        #Calculate the total from what the user inputted
        total_amount=deposit_amount*(1+interest_rate)**number_of_years
        print("R" + str(total_amount))
    elif type_of_interest=="SIMPLE" or type_of_interest=="simple":
        total_amount=deposit_amount*(1+interest_rate*number_of_years)
        print ("R" + str(total_amount))
        
    else:
        print ("Enter Compound or Simple!!")
        
elif users_options=="bond" or users_options=="BOND":
    present_value_of_house=float(input("Enter the present value of your house: "))
    house_interest_rate=float(input("Enter the interest of your house: "))/100
    payment_plan=float(input("In how many months do think you'll be able to repay the loan: "))
    
    total_amount=  (house_interest_rate * present_value_of_house)/(1-(1+house_interest_rate)**(-payment_plan))
    print ("You'll have to pay""R" + str(total_amount) + " " + "every month to settle your house loan in " + " " +  str(payment_plan))
else:
    print("Enter a valid option")
    