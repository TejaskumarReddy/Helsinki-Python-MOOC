
fahrenheit=float(input("Please type in a tempreature(F)"))
celsius=(fahrenheit-32)*(5/9)
print(f"{fahrenheit} degrees Fahrenheit equals {celsius} degrees Celsius")
if celsius<0:
    print("Brr! It's cold in here!")