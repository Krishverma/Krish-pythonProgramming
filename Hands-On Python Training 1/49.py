#area
print("Enter your choice of Triangle")
print("1.Sacalene Triangle")
print("2.Right Triangle")
print("3. Rectangle")
print("4. Square")
print("5. Circle")
x=int(input("Enter Your Choice: "))
if(x==1):
    a=int(input("Entre I side: "))
    b=int(input("Enter II side: "))
    c=int(input("Enter III side: "))
    s=(a+b+c)/2
    area=(s*(s-a)*(s-b)*(s-c))**0.5
    print("Area of Triangle:",area)
elif(x==2):
    b=int(input("Enter Base Length: "))
    h=int(input("Enter height: "))
    area=(b+h)/2
    print("Area: ",area)
elif(x==3):
    l=int(input("Enter Length: "))
    b=int(input("Enter Breath: "))
    area=l*b
    print("Area: ",area)
elif(x==4):
    s=int(input("Enter Side :"))
    area=s*s
    print("Area",area)
elif(x==5):
    r=int(input("Enter Radius: "))
    area=3.14*r*r
    print("Area",area)
else:
    print("Invalid Choice")
