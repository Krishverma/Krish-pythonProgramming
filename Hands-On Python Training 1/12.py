#perimeter of circle, rectangle and triangle
print("Enter your choice of shape")
print("1. Circle")
print("2. Rectangle")
print("3. Triangle")
x=int(input("Enter Your Choice: "))
if(x==1):
    r=int(input("Enter Radius: "))
    peri=2*3.14*r
    print("Perimeter: ",peri)
elif(x==2):
    l=int(input("Enter length: "))
    b=int(input("Enter breath: "))
    peri=2*(l+b)
    print("Perimeter: ",peri)
elif(x==3):
    a=int(input("Enter I side: "))
    b=int(input("Enter II side: "))
    c=int(input("Enter III side: "))
    peri=a+b+c
    print("Perimeter: ",peri)
else:
    print("Invalid Choice")
