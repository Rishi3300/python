ENGLISH=float(input("enter number ENGLISH:"))
HINDI=float(input("enter number HINDI:"))
MATHS =float(input("enter number MATHS:"))
SCIENCE=float(input("enter number SCIENCE:"))
SOCIAL=float(input("enter number SOCIAL:"))
total=ENGLISH+HINDI+MATHS+SCIENCE+SOCIAL
average=total/5
percent=(total/500)*100
print("total no out of 500",total)
print("average",average)
print("percent",percent)
if(percent>90):
   print("a grade")
elif(percent>80 and percent<90):
     print("b grade")
elif(percent>70 and percent<80):
     print("c grade")
elif(percent>60 and percent<70):
     print("c2 grade")
elif(percent>50 and percent<60):
     print("d grade")
elif(percent>40 and percent<50):
     print("e grade")
elif(percent>33 and percent<40):
     print("f grade")
