'''prgm to display a menu for calculating area or perimeter of a circle'''
r=float(input("Enter the radius of the circle"))
print("1. Calculate area")
print("2. Calculate perimeter")
option=int(input("Enter your choice"))
if option==1:
    area=3.14*r*r
    print("Area of the circle is:",area)
else:
    perimeter=2*3.14*r
    print("Perimeter of the circle is:",perimeter)




    
 
