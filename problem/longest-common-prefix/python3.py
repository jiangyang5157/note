# Write a function to find the longest common prefix string amongst an array of strings.

# If there is no common prefix, return an empty string "".


# Example 1:

# Input: strs = ["flower","flow","flight"]
# Output: "fl"
# Example 2:

# Input: strs = ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.


# Constraints:

# 1 <= strs.length <= 200
# 0 <= strs[i].length <= 200
# strs[i] consists of only lowercase English letters.


def main(strs: list[str]) -> str:
    if not strs:
        return ""

    # Optimization: Start with the shortest string as the potential prefix
    shortest = min(strs, key=len)

    for i, ch in enumerate(shortest):
        for other in strs:
            if other == shortest:
                # Skip the shortest string itself
                continue
            if i >= len(other) or other[i] != ch:
                # return prefix up to here
                return shortest[:i] 

    return shortest  # If the loop completes, the shortest string is the common prefix


print(main(["flower", "flow", "flight"]))  # "fl"
print(main(["dog", "racecar", "car"]))  # ""
