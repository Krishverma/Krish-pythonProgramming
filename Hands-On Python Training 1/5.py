#Marks Program
e=int(input("Enter Marks Obtained in English: "))
h=int(input("Enter Marks Obtained in Hindi: "))
m=int(input("Enter Marks Obtained in Maths: "))
sc=int(input("Enter Marks Obtained in Science: "))
cs=int(input("Enter Marks Obtained in Computers: "))
sum=e+h+m+sc+cs
per=sum/5
print("Total Marks Obtained: ",sum," out of 500")
print("Percentage Secured: ",per)
