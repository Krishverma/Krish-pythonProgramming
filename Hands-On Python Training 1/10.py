#volume and surface area of cone, sphere and cylinder
print("Enter your choice of shape")
print("1. Cone")
print("2. Sphere")
print("3. Cylinder")
x=int(input("Enter Your Choice: "))
if(x==1):
    r=int(input("Enter Radius: "))
    l=int(input("Enter Hypotnuese: "))
    v=(1/3)*3.14*r*r*l
    sa=(3.14*r*l)+(3.14*r*r)
    print("Volume: ",v)
    print("Surface Area: ",sa)
elif(x==2):
    r=int(input("Enter Radius: "))
    v=(4/3)*3.14*r*r*r
    sa=4*3.14*r*r
    print("Volume: ",v)
    print("Surface Area: ",sa)
elif(x==3):
    r=int(input("Enter Radius: "))
    h=int(input("Enter Height: "))
    sa=2*3.14*r*(h+r)
    v=3.14*r*r*h
    print("Volume: ",v)
    print("Surface Area: ",sa)
else:
    print("Invalid Choice")
