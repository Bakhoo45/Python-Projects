#Weight Conversion Program

weight = float(input("Enter your  weight: "))
unit = input("Enter the unit (kg/lb): ").strip().lower()

if unit == "kg":
    converted = weight * 2.20462
    print(f"{weight} kg is equal to {round(converted, 2)} lb")
elif unit == "lb":
    converted = weight / 2.20462
    print(f"{weight} lb is equal to {round(converted, 2)} kg")
else:
    print("Invalid unit")