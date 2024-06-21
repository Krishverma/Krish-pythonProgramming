#(1!/1) + (2!/2) + (3!/3) + (4!/4) + (5!/5) + ... + (n!/n)
n=int(input("Enter number: "))
z=0
x=1
for i in range(1,n+1):
        x=i*x
        y=x/i
        z=z+y
print(z)
