#1/2 - 2/3 + 3/4 - 4/5 + 5/6 - ...... upto n terms
n=int(input("Enter Number:"))
a=1
b=2
x=0
y=0
if(n%2==0):  #even terms
    while(a<=(n-1)):
        x=x + (a/b)
        a+=2
        b+=2
    a=2
    b=3
    while(a<=n):
        y=y+(a/b)
        a+=2
        b+=2
    z=x-y
    print(z)

else:
    while(a<=n):
        x=x + (a/b)
        a+=2
        b+=2
    a=a+b
    b=a-b
    a=a-b  #swapping
    b+=2
    while(a<=(n-1)):
        y=y+(a/b)
        a+=2
        b+=2
    z=x-y
    print(z)
