#determining quadrant
x=int(input("Enter X cordinate: "))
y=int(input("Enter Y cordinate: "))
if(x>0 and y>0):
    print("I quadrant")
elif(x<0 and y>0):
    print("II quadrant")
elif(x<0 and y<0):
    print("III quadrant")
elif(x>0 abd y<0):
    print("IV quadrant")
else:
    print("On axis")
