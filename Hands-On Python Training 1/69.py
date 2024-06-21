#armstrong number
n=int(input("Enter any Number:"))
z=n
x=0
while(n>0):
    a=n%10
    n=n//10
    x=x+(a**3)
if(z==x):
    print("Number is Armstrong")

else:
    print("Number is Not Armstrong")
