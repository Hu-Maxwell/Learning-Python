while True: 
    try: 
        values = input("Input two numbers seperated by spaces: ")
        values = list(map(int, values.split()))

        val1 = values[0]
        val2 = values[1]
        result = val1 / val2

        print(f"{result}")

    except ZeroDivisionError: 
        print("You cannot divide by zero.")
    
    except ValueError: 
        print("Please enter a valid number.")

    finally: 
        answer = input("Would you like to continue dividing?")
        if answer.lower() != "yes": 
            print("Thank you for using the division calculator!")
            break