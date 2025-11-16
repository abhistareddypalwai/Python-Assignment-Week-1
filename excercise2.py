Introduction:

This program takes a range of positive integers from the user and checks which numbers within that range are prime. It validates the inputs, identifies prime numbers, and displays them neatly.

def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5) + 1, 2):
        if i < 2:
            continue
        if n % i == 0:
            return False
    return True


def prime_number_generator():
    try:
        # 1. Take two positive integers as input
        start = input("Enter the start of the range: ")
        end = input("Enter the end of the range: ")

        # 2. Validate inputs
        if not start.isdigit() or not end.isdigit():
            print(" Error: Both inputs must be positive integers.")
            return

        start = int(start)
        end = int(end)

        if start <= 0 or end <= 0:
            print(" Error: Inputs must be positive integers greater than zero.")
            return

        if start > end:
            print(" Error: Start of range cannot be greater than end.")
            return

        # 3. Find primes in range
        primes = [num for num in range(start, end + 1) if is_prime(num)]

        # 4. Display formatted output (10 numbers per line)
        print("\n Prime numbers in the given range:")
        for i in range(0, len(primes), 10):
            print(" ".join(f"{p:3}" for p in primes[i:i + 10]))

        if not primes:
            print("No prime numbers found in this range.")

    except Exception as e:
        # 5. Graceful error handling
        print("⚠ An unexpected error occurred:", e)


# Run the program
prime_number_generator()

Conclusion:

The program successfully finds and prints all prime numbers in the given range while handling invalid inputs and errors gracefully.