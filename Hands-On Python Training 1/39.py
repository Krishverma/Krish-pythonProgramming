#greatest of 3
a=int(input("Enter I Number: "))
b=int(input("Enter II Number: "))
c=int(input("Enter III Number: "))
if(a>b):
    if(a>c):
        print(a," is Greatest")
    elif(c>b):
        print(c," is Greatest")
elif(b>c) :
    print(b," is Greatest")
else:
    print("All are Equal")
