#Volume of cube,cuboids and cylider
print("Enter your choice of shape")
print("1. Cube")
print("2. Cuboids")
print("3. Cylinder")
x=int(input("Enter Your Choice: "))
if(x==1):
    a=int(input("Enter Side: "))
    v=a*a*a
    sa=6*a*a
    print("Volume: ",v)
    print("Surface Area: ",sa)
elif(x==2):
    l=int(input("Enter Length: "))
    b=int(input("Enter Breath: "))
    h=int(input("Enter Height:"))
    v=l*b*h
    sa=2*((l*b)+(b*h)+(h*l))
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
