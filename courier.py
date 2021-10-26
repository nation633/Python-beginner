#This program is for a courier company to calculate the cost of sending a parcel

#Stores the price of the product
price_of_package= float(input("Enter price of product: "));

#Stores the Distance of delivery
delivery_in_km= float(input("Enter total distance of delivery in Kilometres: "))


#store constants
AIR_DELIVERY=float(0.36);
FREIGHT_DELIVERY= float(0.25);
FULL_INSURANCE=float(50.00);
LIMITED_INSURANCE=float(25.00);
GIFT=float(15.00);
PRIORITY_DELIVERY=float(100.00);
STANDARD_DELIVERY=float(20.00);


    
#Stores users choices
delivery_type= input("How do you want your product to be delivered? (AIR\FREIGHT): ").upper()
insurance_type= input("What type of insurance do you prefer? (Full\Limited): ").upper()
gift_or_not= input("Is it a gift or not? (gift\ no gift)").upper()
delivery_priority= input("Is your delivery a priority\ not? (Priority\Standard): ").upper()

if delivery_type=="AIR":
        delivery_cost= delivery_in_km * AIR_DELIVERY
else:
        delivery_cost= delivery_in_km * FREIGHT_DELIVERY
        
        
if insurance_type=="FULL":
        additional_cost=FULL_INSURANCE
else:
        additional_cost=LIMITED_INURANCE
        
        
if gift_or_not=="GIFT":
        gift_price=GIFT
else:
        gift_price= 0.00
        
if delivery_priority=="STANDARD":
        delivery_price_cost=STANDARD_DELIVERY
else:
        delivery_price_cost=PRIORITY_DELIVERY

product_final_cost= price_of_package + delivery_cost

package_final_cost= product_final_cost + gift_price + additional_cost + delivery_price_cost

print ("R" + str(product_final_cost))
print ("R" + str(package_final_cost))
        
