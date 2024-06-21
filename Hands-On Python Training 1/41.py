#leap year
n=int(input("Enter any year: "))
if(n%400==0):
    print(n,"is leap year")
elif(n%100==0 or n%4==0):
    print(n,"is not a leap year")
else:
    print(n,"is leap year")
