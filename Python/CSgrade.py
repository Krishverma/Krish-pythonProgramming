#program to print grade of student according to his/her marks

a=int(input("Enter marks of studen (out of 100): "))
if(a>100 or a<0):
    print("Incorrect Marks entered")
elif(a>=75 and a<100):
    print("Distinction")
elif(a>=60 and a<75):
    print("Grade A")
elif(a>=50 and a<60):
    print("Grade B")
elif(a>=40 and a<50):
    print("Grade C")
else:
    print("Grade D")
