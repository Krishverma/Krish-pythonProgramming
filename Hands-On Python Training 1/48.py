#arithmtic calculation
print("What You want to DO")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. True division")
print("5. Floor Division")
print("6. Modulus")
z=int(input("Enter Your Choice:"))
a=int(input("Enter I Number :"))
b=int(input("Enter II Number :"))
if(z==1):
    print(a+b)
elif(z==2):
    print(a-b)
elif(z==3):
    print(a*b)
elif(z==4):
    print(a/b)
elif(z==5):
    print(a//b)
elif(z==6):
    print(a%b)
else:
    print("Invalid Choice")
