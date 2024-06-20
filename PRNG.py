import time
import math

def pseudo_random_number():
    # Get the current time in microseconds
    current_time = time.time()
    
    # Use the current time to seed the randomness
    seed = int((current_time - int(current_time)) * 1e6)
    
    # Apply trigonometric and exponential functions
    random_value = math.tan(seed) * math.exp(-math.sin(seed))
    
    # Normalize the result to the range [0, 1]
    random_value = random_value - int(random_value)
    if random_value < 0:
        random_value = -random_value
    
    return random_value

# Generate a list of pseudo-random numbers
def generate_random_numbers(count):
    random_numbers = []
    for _ in range(count):
        random_numbers.append(pseudo_random_number())
        # Add a small sleep to change the seed for the next number
        time.sleep(0.01)
    return random_numbers

# Main function to handle user interaction
def main():
    while True:
        try:
            # Number of random numbers to generate
            n = int(input("Enter the number of pseudo-random numbers to generate: "))
            
            # Generate and print the random numbers
            random_numbers = generate_random_numbers(n)
            print("Pseudo-random numbers:", random_numbers)
            
            # Ask user if they want to generate more random numbers
            choice = input("Do you want to generate more random numbers? (yes/no): ").lower()
            if choice != 'yes':
                break  # Exit the loop if user does not want more numbers
        
        except ValueError:
            print("Invalid input. Please enter a valid integer.")
    
    print("Program exited.")

if __name__ == "__main__":
    main()
