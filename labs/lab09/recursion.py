# Task 1:
def product_of_digits(x):
    x = abs(x)  
    if x < 10:
        return x
    else:
        return (x % 10) * product_of_digits(x // 10)

# Task 2: 
def array_to_string(a, index):
    if index == len(a) - 1:
        return str(a[index])
    return str(a[index]) + "," + array_to_string(a, index + 1)

# Task 3: 
def log(base, value):
    if value <= 0 or base <= 1:
        raise ValueError("The value must be > 0 and the base must be > 1.")
    if value < base:
        return 0
    return 1 + log(base, value // base)


# Testing
if __name__ == "__main__":
    # Task 1
    print("Task 1: Product of digits")
    print("product_of_digits(234) =", product_of_digits(234)) # 24
    print("product_of_digits(-12) =", product_of_digits(-12)) # 2

    # Task 2
    print("\nTask 2: Array to string")
    sample_array = [1, 2, 3, 4]
    print("array_to_string([1, 2, 3, 4], 0) =", array_to_string(sample_array, 0)) # "1,2,3,4"

    # Task 3
    print("\nTask 3: Recursive Log")
    print("log(10, 123456) =", log(10, 123456)) # 5
    print("log(2, 64) =", log(2, 64)) # 6
    print("log(10, 4567) =", log(10, 4567)) # 3
