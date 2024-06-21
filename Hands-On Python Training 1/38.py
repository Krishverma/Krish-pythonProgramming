#greatest of 3
a=int(input("Enter I Number: "))
b=int(input("Enter II Number: "))
c=int(input("Enter III Number: "))
if(a==b==c):
    print("All are equal")
elif(a>b and a>c):
    print(a," is Greatest")
elif(b>c and b>a):
    print(b," is Greatest")
else:
    print(c, "is Greatest")
