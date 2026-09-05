# Write your solution here
apple=int(input("How many times do you eat in student cafeteria in a week?"))
orange=float(input("The price of a typical student lunch?"))
banana=float(input("How much money do you spend for groceries in a week?"))
weekly=(apple*orange)+banana
daily=(weekly/7)
print()
print("Average food expenditure:")
print(f"Daily: {daily} euros")
print(f"Weekly: {weekly} euros")