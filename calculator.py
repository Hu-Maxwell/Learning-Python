val1 = int(input("Enter value 1: "))
val2 = int(input("Enter value 2: "))

operation = input("Operation? \n")
if operation == "sum": # semicolon : is after if statement
    result = val1 + val2 
elif operation == "subtract": 
    result = val1 - val2
elif operation == "multiply":
    result = val1 * val2
elif operation == "divide":
    result = val1 / val2

print(f"Hello, {result}!")