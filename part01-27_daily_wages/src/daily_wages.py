# Write your solution here
wage=float(input("Houry wage:"))
work=int(input("Hours worked:"))
day=input("Day of the week:")
daily_wage=(wage*work)
if day!= "Sunday":
    print(f"Daily wages: {daily_wage} euros")
if day== "Sunday":
    print(f"Daily wages: {daily_wage*2} euros")