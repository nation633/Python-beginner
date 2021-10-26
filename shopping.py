product1=input("Enter name of your product: ")
product2=input("Enter name of your product: ")
product3=input("Enter name of your product: ")


product1_price=float(input("Enter price of your first product: "))
product2_price=float(input("Enter price of your second product: "))
product3_price=float(input("Enter price of your third product: "))

total= product1_price + product2_price + product3_price
price_average= (product1_price + product2_price + product3_price)/3

print ("The total of" + " " + product1 + ",  " + product2 + ",  " + product3 + ",  " + "is " + "R" + str(total) + " " + "and the average price of the items are" + ",  " + "R" + str(price_average))
