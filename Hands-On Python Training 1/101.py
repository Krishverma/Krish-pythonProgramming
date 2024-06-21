#(1*1) + (2*2) + (3*3) + (4*4) + (5*5) + ... + (n*n)
n=int(input("Enter Terminating Element: "))
x=0
for i in range(1,n+1):
    x=x+(i*i)
print(x)
