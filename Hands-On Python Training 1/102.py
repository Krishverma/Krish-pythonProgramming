#(1) + (1+2) + (1+2+3) + (1+2+3+4) + ... + (1+2+3+4+...+n)
n=int(input("Enter Number:"))
x=0
for i in range(1,n+1):
    for j in range(1,i+1):
        x=x+j

print(x)
