day = int(input("Enter the date 1-31"))
month = int(input("Enter the Month 1-12"))
year = int(input("Enter the Year "))

print(f"Entered year {day:02d}-{month:02d}-{year}")

if(year%4 == 0 and year%100 !=0) or (year%400==0):
    print("Year is Leap")
else:
    print("Year not is Leap")
