a=[ ]
print("You can enter Maximum 50 numbers")
print("Enter 0 to stop entering elements")
for i in range(51):
    x=float(input("Enter Number: "))
    if(x==0):
        break
    else:
        a.append(x)

s=0
for i in a:
    s=s+i
p=1
for i in a:
   p=p*i

hms=s/p
print("Harmonic Sum: ",hms)
