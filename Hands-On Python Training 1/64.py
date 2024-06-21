#armstrong number from 1 to 1000
i=1
while(i<=1000):
    x=0
    n=i
    while(n>0):
        a=n%10
        n=n//10
        x=x+(a**3)
    if(i==x):
        print(i)
    i+=1
