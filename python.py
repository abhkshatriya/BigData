def two_sum(nums, target):
    index_map = {}  # Stores number -> index
    for i, num in enumerate(nums):
        complement = target - num
        if complement in index_map:
            return [index_map[complement], i]
        index_map[num] = i
    return None  # Return None if no pair found

# Example usage
nums = [2, 7, 11, 15]
target = 9
print(two_sum(nums, target))  # Output: [0, 1]
# Programe completed ..git