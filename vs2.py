def majority_elements(nums):
    if not nums:
        return []

    n = len(nums)
    threshold = n // 3

    # Dictionary to store the count of each element
    count_dict = {}

    # Iterate through the array and count occurrences
    for num in nums:
        if num in count_dict:
            count_dict[num] += 1
        else:
            count_dict[num] = 1

    # Filter elements that appear more than ⌊ n/3 ⌋ times
    result = [num for num, count in count_dict.items() if count > threshold]

    return result

# Get user input for the integer array
while True:
    try:
        user_input = input("Enter integers separated by spaces: ")
        nums = list(map(int, user_input.split()))
        break
    except ValueError:
        print("Invalid input. Please enter integers separated by spaces.")

# Find majority elements and print the result
result = majority_elements(nums)
print(f"Elements appearing more than ⌊ n/3 ⌋ times: {result}")
