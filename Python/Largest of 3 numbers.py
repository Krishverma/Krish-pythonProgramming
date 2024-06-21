'''prgm to accept three integers and print the largest of the three'''
x=int(input("Enter the first number:"))
y=int(input("Enter the second number:"))
z=int(input("Enter the third number:"))
if x>y:
    max=x
if y>z:
    max=y
if z>x:
    max=z
print("The largest of the three numbers will be:",max)


