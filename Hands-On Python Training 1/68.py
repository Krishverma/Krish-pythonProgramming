#palindrome number
n=int(input("Enter Any Number : "))
z=n
rev=0
while(n>0):
    a=n%10
    n=n//10
    rev=(10*rev)+a
if(z==rev):
    print("Number is Palindrome")
else:
    print("Number is Not Palindrome")
