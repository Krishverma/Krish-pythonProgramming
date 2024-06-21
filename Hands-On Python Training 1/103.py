#1! + 2! + 3! + 4! + 5! + ... + n!
n=int(input("Enter number: "))
z=0
x=1
for i in range(1,n+1):
        x=i*x
        z=z+x
print(z)
