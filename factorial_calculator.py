def calculate_factorial(n): 
    if n == 0 or n == 1: 
        return 1
    return n * calculate_factorial(n-1)


val = int(input("Input a number: "))
result = calculate_factorial(val)
print(f"Factorial: {result}")