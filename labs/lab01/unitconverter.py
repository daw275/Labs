def convert_units(value, unit):
    conversions = {
        "cm": ("in", value / 2.54),
        "in": ("cm", value * 2.54),
        "yd": ("m", value * 0.9144),
        "m": ("yd", value / 0.9144),
        "oz": ("g", value * 28.349523125),
        "g": ("oz", value / 28.349523125),
        "lb": ("kg", value * 0.45359237),
        "kg": ("lb", value / 0.45359237)
    }

    if unit in conversions:
        new_unit, converted_value = conversions[unit]
        return f"{value} {unit} = {converted_value:.2f} {new_unit}"
    else:
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
