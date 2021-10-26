#This program determines whether a year is a leap year is to test whether it is a multiple of 4.

#Store users inputs.
year=int(input("What year do you want to start with?: "))
number_of_years=int(input("How many years do you want to check?: "))

for i in range(year,year + number_of_years +1):
    if i % 4==0:
        print(str(i) + "is a leap year")
    else:
        print(str(i) + "is not a leap year")