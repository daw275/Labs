def convert_units(value, unit):
    match unit:
        case "cm":
            return f"{value} cm = {value / 2.54:.2f} in"
        case "in":
            return f"{value} in = {value * 2.54:.2f} cm"
        case "yd":
            return f"{value} yd = {value * 0.9144:.2f} m"
        case "m":
            return f"{value} m = {value / 0.9144:.2f} yd"
        case "oz":
            return f"{value} oz = {value * 28.349523125:.2f} g"
        case "g":
            return f"{value} g = {value / 28.349523125:.2f} oz"
        case "lb":
            return f"{value} lb = {value * 0.45359237:.2f} kg"
        case "kg":
            return f"{value} kg = {value / 0.45359237:.2f} lb"
        case _:
            return "Invalid unit"

def main():
    try:
        user_input = input("Enter a value followed by a unit (Example: '10 cm'): ").strip()
        
        value_str, unit = user_input.split(" ", 1)  
        value = float(value_str)

        result = convert_units(value, unit)
        print(result)

    except ValueError:
        print("Invalid input")

if __name__ == "__main__":
    main()
