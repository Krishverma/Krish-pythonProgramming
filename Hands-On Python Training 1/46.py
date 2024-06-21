# day according to day number
a=['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
x=int(input("Enter day number: "))
b=[1,2,3,4,5,6,7]
c=a[x-1]
if(x in b):
    print(c)
else:
    print("Invalid Choice")
