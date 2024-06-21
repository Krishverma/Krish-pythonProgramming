#harshad number
n=int(input("Enter any Number: "))
z=n
x=0
while(n>0):
    a=n%10
    n=n//10
    x=x+a
if(z%x==0):
    print("Number is Harshad")
else:
    print("Number is Not Harshad")
