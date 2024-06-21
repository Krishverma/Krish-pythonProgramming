z=6
for i in range(1,z):
    for j in range(1,z-i):
        print(" ",end=" ")
    for k in range(1,i+i):
        print(k-i,end=" ")
    i+=1
    print()

