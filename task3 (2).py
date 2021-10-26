import math

#Array that stores numbers from 0 to 20
a=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

#This loop will reverse the numbers stored in the array

while True:
    a.reverse()
    print(a)
    
    break

#This loop will check for all even numbers in the array then display them all
for i in a:
    #Checks for even numbers in array
    if i % 2 == 0:
        print (i)
        
while True:
    print("*" "\n**" "\n***")
            
    break
 
 # Calculates lcm of two numbers      
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
gcd = str(math.gcd(num1,num2))       

print("GCD= " + gcd)
