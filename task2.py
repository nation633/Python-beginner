#This program will be used to calculate the area that the foundation of a building covers

#Stores the shape of the building
shape_of_building=input("Enter shape of building ((square, rectangular or round): ").lower()


if shape_of_building=="square":
    length_of_building=int(input("Enter the length of the building: "))
    area_of_building=length_of_building ** length_of_building
    print ("The area of the foundation is" + " " + str(area_of_building))
    
elif shape_of_building=="rectangular":
    length_of_building=int(input("Enter the length of the building: "))    
    width_of_building=int(input("Enter the width of the building: "))
    area_of_building=length_of_building * width_of_building
    print ("The area of the foundation is" + " " + str(area_of_building))
      
else:
    PI=int(3.14159)
    radius_of_building=int(input("Enter the radius of the circular building: "))
    area_of_building=PI * (radius_of_building ** radius_of_building)
    print ("The area of the foundation is" + " " + str(area_of_building))