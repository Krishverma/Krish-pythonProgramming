#roots of equation
a=int(input("Enter coefficient of x^2 :"))
b=int(input("Enter coefficient of x :"))
c=int(input("Enter constant :"))
d=((b**2)-(4*a*c))
x1=(-b + (d**0.5))/(2*a)
x2=(-b - (d**0.5))/(2*a)
print("Roots are: ",x1,"and",x2)
