#sum of digits
n=int(input("Enter any Number: "))
x=0
while(n>0):
    a=n%10
    n=n//10
    x=x+a
print(x)
    
