#prime number
n=int(input("Enter any Number: "))
count=0
i=2
while(i<=(n//2)):
    if(n%i==0):
        count+=1
    i+=1
if(count==0):
    print("Prime Number")
else:
    print("Not a Prime Number")
