#Gravitational force b/w two objects
m1=float(input("Enter Mass of I object in Kg: "))
m2=float(input("Enter Mass of II object in Kg: "))
r=float(input("Enter distance between the objects: "))
f=(6.67*m1*m2)/(r*r) # 10^11 does not play role in multilication so it is printed directly
print("Force: ",f,"X 10^11")
