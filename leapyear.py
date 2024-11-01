year=int(input("Enter the Year"))
if(year==2000):
    print(year, " is a leap year")
elif(year%4==0):
    print(year," is a leap year")
else:
    print(year,"is not leap year")
