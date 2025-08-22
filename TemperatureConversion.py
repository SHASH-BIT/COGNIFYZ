temperature = int(input("Enter the temperature value : "))
unit = input("Enter the unit (C is for Celsius , F is for Fahrenheit):")

if unit =="C":
    fahrenheit = (temperature * 9/5)+32
    print(f"{temperature}°C is equals to {fahrenheit}°F ")

elif unit == "F":
    celcius = (temperature - 32) * 5/9
    print(f"{temperature}°F is equals to {celcius}°C")
else:
    print("INVALID UNIT ENTERED .    Please enter C or F .")