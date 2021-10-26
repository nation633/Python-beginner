#This program that calculates a person's BMI

#Gets and stores the users weight and height
weight_in_kg= float(input("Enter your weight in KG's: "))
height_in_m= float(input("Enter your height in meteres: "))

BMI=(weight_in_kg)/((height_in_m)*(height_in_m))

if BMI>=30:
    print ("Your BMI is" + "" + str(BMI) + " " + "You are obese!")
elif BMI>=25 and BMI<30:
    print ("Your BMI is" + "" + str(BMI) + " " + "You are over weight!")
elif BMI>=18.5 and BMI<25:
    print ("Your BMI is" + "" + str(BMI) + " " + "You are nomal!")
else:
    print ("Your BMI is" + "" + str(BMI) + " " + "You are underweight!!!")
    

