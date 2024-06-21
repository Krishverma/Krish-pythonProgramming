#sum of all prime numbers from 1to 1000
z=0
for j in range(2,1001):
    count=0
    i=2
    while(i<=(j//2)):
        if(j%i==0):
            count+=1
        i+=1
    if(count==0):
        z=z+j
print(z)
