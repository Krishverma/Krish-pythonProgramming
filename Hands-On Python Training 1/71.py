#prime numbers b/w 1 to 500

for j in range(2,501):
    count=0
    i=2
    while(i<=(j//2)):
        if(j%i==0):
            count+=1
        i+=1
    if(count==0):
        print(j)
