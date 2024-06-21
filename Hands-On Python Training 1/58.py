# factorial of a number
print("From Which Method")
print("1. For Loop")
print("2. while Loop")
ch=int(input("Enter Choice: "))
a=int(input("Enter any Number: "))
x=1
if(ch==1):
    l=a+1
    for i in range(2,l):
        x=i*x
    print(x)
elif(ch==2):
    i=1
    while(i<=a):
        x=i*x
        i+=1
    print(x)
else:
    print("Invalid Choice")
