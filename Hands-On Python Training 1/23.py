# sWapping using XOr
a=int(input("Enter I Number: "))
b=int(input("Enter II Number: "))
print("Number before swapping: ",a,"and",b)
a=a^b
b=(a^b)
a=(a^b)
print("Number after swapping: ",a,"and",b)
