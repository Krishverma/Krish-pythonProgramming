#swapping
#area of trapezium, rhombus and parallelogram
print("Enter your choice of shape")
print("1. With III Variable")
print("2. Without III variable")
x=int(input("Enter Your Choice: "))
if(x==1):
    a=int(input("Enter I Number: "))
    b=int(input("Enter II Number: "))
    print("Number before swapping: ",a,"and",b)
    c=a
    a=b
    b=c
    print("Number after swapping: ",a,"and",b)
elif(x==2):
    a=int(input("Enter I Number: "))
    b=int(input("Enter II Number: "))
    print("Number before swapping: ",a,"and",b)
    a=a+b
    b=a-b
    a=a-b
    print("Number after swapping: ",a,"and",b)
else:
    print("Invalid Choice")
