def is_prime(num):
    """
    Checks if a given number is prime.
    A number is prime if it is greater than 1 and has no divisors other than 1 and itself.
    """
    if num <= 1:
        return False  # Numbers less than or equal to 1 are not prime
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False  # If divisible by any number other than 1 and itself, it's not prime
    return True  # If no divisors found, it's prime

def print_primes_in_range(start, end):
    """
    Prints all prime numbers within a specified range (inclusive).
    """
    print(f"Prime numbers between {start} and {end}:")
    for number in range(start, end + 1):
        if is_prime(number):
            print(number)

# Call the function to print prime numbers between 1 and 100
print_primes_in_range(1, 100)