def length_of_last_word(s):
    words = s.split()

    # Return the length of the last word
    return len(words[-1])

# Get user input for the string
while True:
    user_input = input("Enter a string (1 <= length <= 10^4, English letters and spaces only, at least one word): ").strip()

    # Check constraints
    if 1 <= len(user_input) <= 10**4 and all(char.isalpha() or char.isspace() for char in user_input) and ' ' in user_input:
        break
    else:
        print("Invalid input. Please follow the constraints.")

# Calculate and print the length of the last word
result = length_of_last_word(user_input)
print(f"The length of the last word is: {result}")
