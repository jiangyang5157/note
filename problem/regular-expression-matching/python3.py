# https://leetcode.com/problems/regular-expression-matching/description/?envType=problem-list-v2&envId=dynamic-programming

# Given an input string s and a pattern p, implement regular expression matching with support for '.' and '*' where:

# '.' Matches any single character.​​​​
# '*' Matches zero or more of the preceding element.
# The matching should cover the entire input string (not partial).

 

# Example 1:

# Input: s = "aa", p = "a"
# Output: false
# Explanation: "a" does not match the entire string "aa".
# Example 2:

# Input: s = "aa", p = "a*"
# Output: true
# Explanation: '*' means zero or more of the preceding element, 'a'. Therefore, by repeating 'a' once, it becomes "aa".
# Example 3:

# Input: s = "ab", p = ".*"
# Output: true
# Explanation: ".*" means "zero or more (*) of any character (.)".
 

# Constraints:

# 1 <= s.length <= 20
# 1 <= p.length <= 20
# s contains only lowercase English letters.
# p contains only lowercase Englisxh letters, '.', and '*'.
# It is guaranteed for each appearance of the character '*', there will be a previous valid character to match.
    
def isMatch(s: str, p: str) -> bool:
    """
    Determines if the input string 's' matches the pattern 'p' according to the rules of regular expression matching.

    Args:
        s: The input string (lowercase English letters only).
        p: The pattern string (lowercase English letters, '.', and '*' only).

    Returns:
        True if 's' matches 'p', False otherwise.
    """

    s_len, p_len = len(s), len(p)
    
    # dp[i][j] represents whether s[:i] matches p[:j]
    dp = [[False] * (p_len + 1) for _ in range(s_len + 1)]
    
    # Empty string matches empty pattern
    dp[0][0] = True
    
    # Handle patterns starting with '*' (e.g., "a*", ".*", "c*a*")
    for j in range(1, p_len + 1):
        if p[j - 1] == '*':
            dp[0][j] = dp[0][j - 1 - 1]

    for i in range(1, s_len + 1):
        for j in range(1, p_len + 1):
            if p[j - 1] == '.' or p[j - 1] == s[i - 1]:
                # If current characters match (or '.' in pattern), check previous subproblem
                dp[i][j] = dp[i - 1][j - 1]
            elif p[j - 1] == '*':
                # '*' case:
                # 1. Zero occurrences of the preceding element: check dp[i][j-2]
                # 2. One or more occurrences: check if preceding element matches current char in s AND dp[i-1][j]
                dp[i][j] = dp[i][j - 1 - 1] or (
                    (p[j - 2] in {'.', s[i - 1]}) and dp[i - 1][j]
                )
            else:
                # Characters don't match, and no '*'
                dp[i][j] = False

    return dp[s_len][p_len]


print(isMatch("aa", "a"))  # Output: False
print(isMatch("aa", "a*"))  # Output: True
print(isMatch("ab", ".*"))  # Output: True
print(isMatch("aab", "c*a*b")) # Output: True
print(isMatch("mississippi", "mis*is*p*.")) # Output: False
