#area of trapezium, rhombus and parallelogram
print("Enter your choice of shape")
print("1. Trapezium")
print("2. Rhombus")
print("3. Paralellogram")
x=int(input("Enter Your Choice: "))
if(x==1):
    a=int(input("Enter I Non-parallel side: "))
    b=int(input("Enter II Non=parallel side: "))
    h=int(input("Enter Height: "))
    area=((a+b)/2)*h
    print("Area: ",area)
elif(x==2):
    a=int(input("Enter length of I diagonal: "))
    b=int(input("Enter length of II diagonal: "))
    area=(a+b)/2
    print("Area: ",area)
elif(x==3):
    b=int(input("Enter Base length: "))
    h=int(input("Enter Height: "))
    area=b*h
    print("Area: ",area)
else:
    print("Invalid Choice")
