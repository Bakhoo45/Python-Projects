#Temperature Conversion Program

temperature = float(input("Enter the temperature: "))
unit = input("Enter the unit (C/F): ").strip().lower()

if unit == "c":
    converted = (temperature * 9/5) + 32
    print(f"{temperature}°C is equal to {round(converted, 1)}°F")
elif unit == "f":
    converted = (temperature - 32) * 5/9
    print(f"{temperature}°F is equal to {round(converted, 1)}°C")
else:
    print("Invalid unit")
