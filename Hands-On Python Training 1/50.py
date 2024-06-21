#Grade
e=int(input("Enter Marks Obtained in English: "))
h=int(input("Enter Marks Obtained in Hindi: "))
m=int(input("Enter Marks Obtained in Maths: "))
sc=int(input("Enter Marks Obtained in Science: "))
cs=int(input("Enter Marks Obtained in Computers: "))
sum=e+h+m+sc+cs
per=sum/5
print("Total Marks Obtained: ",sum," out of 500")
print("Percentage Secured: ",per)
if(per>=90 and per<=100):
    print("Grade A")
elif(per>=80 and per<90):
    print("Grade B")
elif(per>=60 and per<80):
    print("Grade C")
elif(per>=50 and per<60):
    print("Grade D")
elif(per>=40 and per<50):
    print("Grade E")
else:
    print("Fail")
