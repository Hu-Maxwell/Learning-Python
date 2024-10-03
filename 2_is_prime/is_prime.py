def is_prime(n): # this is a function 
    if n < 2: 
        return False
    for i in range(2, int(n**.5) + 1): 
        if n % i == 0:
            return False
    return True 

while True: 
    num = int(input("Enter a number: "))
    if is_prime(num): 
        print(f"The number {num} is prime.")
    else: 
        print(f"The number {num} is not prime!")

    answer = input("Do you want to try another number? Y/N ")
    if answer.lower() == "n":
        print("Goodbye!")
        break 
