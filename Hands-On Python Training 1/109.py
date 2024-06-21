n=int(input("Enter Number:"))
a=1
b=2
print(a,b,end=" ")
for i in range(3,n+1):
    if(i%2==1):
        a=a*3
        print(a,end=" ")
    else:
        b=b*3
        print(b,end=" ")
