'''Sum after every digit in a list'''
mylist=eval(input("Enter the list:"))
sum=0
for i in range(0,len(mylist)):
    sum+=mylist[i]
    print("Total:",sum)
