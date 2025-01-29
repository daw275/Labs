import math

def main():
    try:
        radius = float(input("Enter the radius of the circle: "))

        if radius < 0:
            print("Radius cannot be negative.")
            return

        area = math.pi * (radius ** 2)
        perimeter = 2 * math.pi * radius

        print(f"The circle with radius {radius} has an area of {area:.2f} and a perimeter of {perimeter:.2f}.")
    
    except ValueError:
        print("Invalid input")

if __name__ == "__main__":
    main()
