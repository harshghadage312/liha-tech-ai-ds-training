"""Write a Python program to swap first and last digits of a number."""
# Take integer input from the user
num = int(input("Enter any number: "))

# Keep original number intact and handle single digits
if num < 10:
    result = num
else:
    # 1. Find the last digit
    last_digit = num % 10

    # 2. Find the first digit and count the place value (multiplier)
    first_digit = num
    multiplier = 1

    while first_digit >= 10:
        first_digit = first_digit // 10
        multiplier = multiplier * 10

    # 3. Extract the middle part of the number
    # (num % multiplier) removes the first digit
    # ( // 10) removes the last digit
    middle_part = (num % multiplier) // 10

    # 4. Combine them back together in reverse order
    result = (last_digit * multiplier) + (middle_part * 10) + first_digit

# Print the final swapped number
print(f"Swapped number: {result}")


