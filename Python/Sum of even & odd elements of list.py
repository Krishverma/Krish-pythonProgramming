mylist=eval(input("Enter the list:"))
sume=sumo=0
for i in mylist:
    if i%2==1:
        sumo+=i
    else:
        sume+=i
print("Odd:",sumo)
print("Even:",sume)
