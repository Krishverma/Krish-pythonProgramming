# compute nCr
n=int(input("Enter Value of n:"))
r=int(input("Enter Value of r:"))
nf=1
for i in range(2,n+1):
    nf=i*nf
rf=1
for i in range(2,r+1):
    rf=i*rf
n_rf=1
for i in range(2,n-r+1):
    n_rf=i*n_rf

ncr=nf/(rf*n_rf)
print(ncr)
