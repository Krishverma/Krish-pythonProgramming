mylist=eval(input("Enter the list:"))
evecount=oddcount=0
for i in range(len(mylist)):
    if i%2==0:
        evecount+=1
    else:
        oddcount+=1
print("Even:",evecount)
print("Odd:",oddcount)
