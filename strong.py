import math

def is_strong_number(num):
    """
    Checks if a given number is a strong number.
    A strong number is a number whose sum of the factorial of its digits is equal to the number itself.
    For example, 145 is a strong number because 1! + 4! + 5! = 1 + 24 + 120 = 145.
    """
    if num < 0:
        return False  # Strong numbers are typically defined for non-negative integers.
    
    original_num = num
    sum_of_factorials = 0
    
    # Handle the case of 0 separately, as 0! is 1, but 0 is not a strong number by common definition.
    if num == 0:
        return False

    while num > 0:
        digit = num % 10
        sum_of_factorials += math.factorial(digit)
        num //= 10
        
    return sum_of_factorials == original_num

def print_strong_numbers_in_range(start, end):
    """
    Prints all strong numbers within a specified range (inclusive).
    """
    print(f"Strong numbers between {start} and {end}:")
    for number in range(start, end + 1):
        if is_strong_number(number):
            print(number)

# Call the function to print strong numbers between 1 and 5000
print_strong_numbers_in_range(1, 5000)