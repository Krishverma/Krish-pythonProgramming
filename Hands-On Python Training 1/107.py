#[(1^1)/1!] + [(2^2)/2!] + [(3^3)/3!] + [(4^4)/4!] + [(5^5)/5!] + ... + [(n^n)/n!]
n=int(input("Enter Terminating Element: "))
x=0
y=1
for i in range(1,n+1):
    y=i*y
    x=x+((i**i)/y)
print(x)
