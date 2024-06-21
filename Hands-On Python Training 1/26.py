#different units to seconds
print("Enter choice number from which unit you want to convert")
print("1. Minutes")
print("2. Hours")
print("3. Days")
print("4. Weeks")
z=int(input("Enter Choice: "))
if(z==1):
    a=int(input("Enter Minutes: "))
    b=a*60
    print(b," seconds")
elif(z==2):
    a=int(input("Enter Hours: "))
    b=a*60*60
    print(b," seconds")
elif(z==3):
    a=int(input("Enter Days: "))
    b=a*60*60*24
    print(b," seconds")
elif(z==4):
    a=int(input("Enter Weeks: "))
    b=a*60*60*24*7
    print(b," seconds")
else:
    print("Invalid Choice")
