
def two_sum(nums: list[int], target: int) -> list[int]:
    num_to_index = {}  # Dictionary to store numbers and their indices

    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_to_index:
            return [num_to_index[complement], i] 
        num_to_index[num] = i

    return []  # No solution found


print(two_sum([1,2,3,4], 3))