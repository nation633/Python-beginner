#This program will print out all the even numbers from 1 upt to the number given by the user
#Store the users input
sum1=int(input("enter your number: "))
#counter
i=0
#Repetition structure
while i<=sum1:
    if i % 2 ==0:
        print(i)
    i+=1
    