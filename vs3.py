def shortest_palindrome(s):
    rev_s = s[::-1]
    
    for i in range(len(s) + 1):
        if s.startswith(rev_s[i:]):
            return rev_s[:i] + s

# Get user input for the string
user_input = input("Enter a string: ")

# Find the shortest palindrome and print the result
result = shortest_palindrome(user_input)
print(f"The shortest palindrome is: {result}")
