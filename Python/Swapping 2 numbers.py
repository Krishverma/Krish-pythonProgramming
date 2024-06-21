'''prgm to swap two numbers without using third variable'''
a=int(input("Enter the first number"))
b=int(input("Enter the second number"))
print("The numbers before swaping:",a,b)
a=a+b
b=a-b
a=a-b
print("The numbers after swapping:",a,b)



