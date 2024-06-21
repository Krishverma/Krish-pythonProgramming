#perfect number
n=int(input("Enter any Number: "))
z=0
for i in range(1,(n//2)+1,1):
    if(n%i==0):
        z=z+i
if(z==n):
        print("Number is Perfect")
else:
        print("Number is not Perfect")
