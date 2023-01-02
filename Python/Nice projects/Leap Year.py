year = int(input("Enter a year to check whether it's a leap year: "))

if (year%4 == 0 and year%100!=0 and year%400!=0):
    print(f"The year {year} is a leap year.")
elif (year%4 == 0 and year%100==0 and year%400==0):
    print(f"The year {year} is a leap year.")
else:
    print(f"The year {year} is not a leap year.")

# version number 2

if (year%4 == 0):
    if(year%100 == 0):
        if(year%400 == 0):
            print("Leap year")
        else:
            print(f"The year {year} is not a leap year.")
    else:
        print(f"The year {year} is not a leap year.")
        
else: 
    print(f"The year {year} is not a leap year.")
    