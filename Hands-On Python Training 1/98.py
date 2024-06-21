#Sum of gP
n=float(input("Enter Number of Terms: "))
a=float(input("Enter the First term of GP: "))
r=float(input("Enter Common ratio: "))
s= (a*(r**n -1))/(r-1)
print("Sum of GP : ",s)
