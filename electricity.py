unit=float(input("enter the number of unit:"))
first100=unit*5
minus1=unit-200
ex200=(100*5)+(minus1*10)
if(unit>0):
  if(unit<=100):
    print("NO CHARGE")
elif(unit>100 and unit<=200):
 print("5 per unit:  Your bill Is ",first100)
elif(unit>200):
 print("10 per unit: Your bill Is ",ext200)
else:
 print("you have the value less than 0")
 
