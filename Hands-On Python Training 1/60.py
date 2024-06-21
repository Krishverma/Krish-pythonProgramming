#reverse of a given number
n=int(input("Enter Any Number : "))
rev=0
while(n>0):
    a=n%10
    n=n//10
    rev=(10*rev)+a
print(rev)
