import math

def main():
    a = float(input("Enter the length of the first side: "))
    b = float(input("Enter the length of the second side: "))

    c = math.sqrt(a ** 2 + b ** 2)

    print(f"The hypotenuse is {c:.2f}")

if __name__ == "__main__":
    main()
