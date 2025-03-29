# https://leetcode.com/problems/encode-and-decode-tinyurl/description/

# Note: This is a companion problem to the System Design problem: Design TinyURL.
# TinyURL is a URL shortening service where you enter a URL such as https://leetcode.com/problems/design-tinyurl and it returns a short URL such as http://tinyurl.com/4e9iAk. Design a class to encode a URL and decode a tiny URL.

# There is no restriction on how your encode/decode algorithm should work. You just need to ensure that a URL can be encoded to a tiny URL and the tiny URL can be decoded to the original URL.

# Implement the Solution class:

# Solution() Initializes the object of the system.
# String encode(String longUrl) Returns a tiny URL for the given longUrl.
# String decode(String shortUrl) Returns the original long URL for the given shortUrl. It is guaranteed that the given shortUrl was encoded by the same object.
 

# Example 1:

# Input: url = "https://leetcode.com/problems/design-tinyurl"
# Output: "https://leetcode.com/problems/design-tinyurl"

# Explanation:
# Solution obj = new Solution();
# string tiny = obj.encode(url); // returns the encoded tiny url.
# string ans = obj.decode(tiny); // returns the original url after decoding it.
 

# Constraints:

# 1 <= url.length <= 104
# url is guranteed to be a valid URL.

class Solution:
    def __init__(self):
        self.long_to_short = {}  # Dictionary to store long URL to short URL mapping
        self.short_to_long = {}  # Dictionary to store short URL to long URL mapping
        self.base_url = "http://encode.url/"
        self.counter = 0

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        if not longUrl:
            return ""
        
        if longUrl in self.long_to_short:
            return self.long_to_short[longUrl]

        self.counter += 1
        short_url_id = self.get_short_url_id(self.counter)
        shortUrl = self.base_url + short_url_id

        self.long_to_short[longUrl] = shortUrl
        self.short_to_long[shortUrl] = longUrl
        return shortUrl

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        if not shortUrl:
            return ""
        
        return self.short_to_long.get(shortUrl)

    def get_short_url_id(self, n: int) -> str:
        """
        Generates a unique short URL ID based on an integer counter.
        Uses base62 encoding (a-zA-Z0-9).
        """
        characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
        base = len(characters)
        short_url_id = ""
        while n > 0:
            short_url_id = characters[n % base] + short_url_id
            n //= base
        return short_url_id if short_url_id else "a"


# Example Usage (for testing):
solution = Solution()
long_url = "https://leetcode.com/problems/design-tinyurl"
short_url = solution.encode(long_url)
print(f"Encoded URL: {short_url}")
decoded_url = solution.decode(short_url)
print(f"Decoded URL: {decoded_url}")

long_url2 = "https://www.google.com"
short_url2 = solution.encode(long_url2)
print(f"Encoded URL: {short_url2}")
decoded_url2 = solution.decode(short_url2)
print(f"Decoded URL: {decoded_url2}")

print(solution.decode("http://tinyurl.com/b"))
