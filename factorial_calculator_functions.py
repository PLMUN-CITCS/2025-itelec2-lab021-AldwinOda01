def get_non_negative_integer() -> int:
   
    while True:
        try:
            number = int(input("Enter a non-negative integer: "))
            if number >= 0:
                return number
            print("Invalid input. Please enter a non-negative integer.")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

def calculate_factorial(n: int) -> int:
    
    factorial = 1
    for i in range(1, n + 1):
        factorial *= i
    return factorial

user_number = get_non_negative_integer()
factorial_result = calculate_factorial(user_number)

print(f"The factorial of {user_number} is: {factorial_result}")
