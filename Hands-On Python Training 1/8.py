#area of scalene triangle
print("Enter your choice of Triangle")
print("1.Sacalene Triangle")
print("2.Right Triangle")
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
else:
    print("Invalid Choice")
