#disariium number
n=int(input("Enter any Number: "))
a=n
count=0
while(n>1):
    n=n//10
    count+=1
place=count-1
x=0
for i in range(1,count+1):
    a=a%(10**place)
    x=x+a**i
    place-=1
print(x)
