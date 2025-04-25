def number_to_binary(s):
    if s < 0:
        return '-' + bin(s)[3:]  # Handle negative numbers
    return bin(s)[2:]  # Handle positive numbers

# Example usage
s = int(input("Enter a number: "))  # Allow user input
binary_representation = number_to_binary(s)
print(f"The binary representation of {s} is: {binary_representation}")
