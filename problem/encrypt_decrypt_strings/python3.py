# https://leetcode.com/problems/encrypt-and-decrypt-strings/description/

# You are given a character array keys containing unique characters and a string array values containing strings of length 2. You are also given another string array dictionary that contains all permitted original strings after decryption. You should implement a data structure that can encrypt or decrypt a 0-indexed string.

# A string is encrypted with the following process:

# For each character c in the string, we find the index i satisfying keys[i] == c in keys.
# Replace c with values[i] in the string.
# Note that in case a character of the string is not present in keys, the encryption process cannot be carried out, and an empty string "" is returned.

# A string is decrypted with the following process:

# For each substring s of length 2 occurring at an even index in the string, we find an i such that values[i] == s. If there are multiple valid i, we choose any one of them. This means a string could have multiple possible strings it can decrypt to.
# Replace s with keys[i] in the string.
# Implement the Encrypter class:

# Encrypter(char[] keys, String[] values, String[] dictionary) Initializes the Encrypter class with keys, values, and dictionary.
# String encrypt(String word1) Encrypts word1 with the encryption process described above and returns the encrypted string.
# int decrypt(String word2) Returns the number of possible strings word2 could decrypt to that also appear in dictionary.
 

# Example 1:

# Input
# ["Encrypter", "encrypt", "decrypt"]
# [[['a', 'b', 'c', 'd'], ["ei", "zf", "ei", "am"], ["abcd", "acbd", "adbc", "badc", "dacb", "cadb", "cbda", "abad"]], ["abcd"], ["eizfeiam"]]
# Output
# [null, "eizfeiam", 2]

# Explanation
# Encrypter encrypter = new Encrypter([['a', 'b', 'c', 'd'], ["ei", "zf", "ei", "am"], ["abcd", "acbd", "adbc", "badc", "dacb", "cadb", "cbda", "abad"]);
# encrypter.encrypt("abcd"); // return "eizfeiam". 
#                            // 'a' maps to "ei", 'b' maps to "zf", 'c' maps to "ei", and 'd' maps to "am".
# encrypter.decrypt("eizfeiam"); // return 2. 
#                               // "ei" can map to 'a' or 'c', "zf" maps to 'b', and "am" maps to 'd'. 
#                               // Thus, the possible strings after decryption are "abad", "cbad", "abcd", and "cbcd". 
#                               // 2 of those strings, "abad" and "abcd", appear in dictionary, so the answer is 2.
 

# Constraints:

# 1 <= keys.length == values.length <= 26
# values[i].length == 2
# 1 <= dictionary.length <= 100
# 1 <= dictionary[i].length <= 100
# All keys[i] and dictionary[i] are unique.
# 1 <= word1.length <= 2000
# 2 <= word2.length <= 200
# All word1[i] appear in keys.
# word2.length is even.
# keys, values[i], dictionary[i], word1, and word2 only contain lowercase English letters.
# At most 200 calls will be made to encrypt and decrypt in total.


from collections import defaultdict
from typing import List


class Encrypter:

    def __init__(self, keys: List[str], values: List[str], dictionary: List[str]):
        self.key_to_value = dict(zip(keys, values))
        self.value_to_keys = defaultdict(list)
        for key, value in zip(keys, values):
            self.value_to_keys[value].append(key)
        self.valid_words = set(dictionary)
        self.encrypted_words_count = defaultdict(int)
        for word in dictionary:
            encrypted_word = self.encrypt(word)
            if encrypted_word:
                self.encrypted_words_count[encrypted_word] += 1

    def encrypt(self, word1: str) -> str:
        encrypted_word = ""
        for char in word1:
            if char not in self.key_to_value:
                return ""
            encrypted_word += self.key_to_value[char]
        return encrypted_word

    def decrypt(self, word2: str) -> int:
        if len(word2) % 2 != 0:
            return 0
        
        return self.encrypted_words_count[word2]


# Example Usage:
keys = ['a', 'b', 'c', 'd']
values = ["11", "22", "11", "44"]
dictionary = ["abad", "abcd", "cbcd", "dd"]
encrypter = Encrypter(keys, values, dictionary)
print("abcd <-encrypt> " + str(encrypter.encrypt("abcd"))) # 11221144
print("a <-encrypt> " + str(encrypter.encrypt("a"))) #11
print("b <-encrypt> " + str(encrypter.encrypt("b"))) #22
print("c <-encrypt> " + str(encrypter.encrypt("c"))) #11
print("d <-encrypt> " + str(encrypter.encrypt("d"))) #44
print("dcb <-encrypt> " + str(encrypter.encrypt("dcb"))) #441122
# 11 maps to 'a' or 'c'
# 22 maps to 'b'
# 44 maps to 'd'
# do 11221144 maps to: abad, abcd, cbcd, cbad. only 3 of them found in dictionary
print("11221144 <decrypt-> " + str(encrypter.decrypt("11221144")))
print("44 <decrypt-> " + str(encrypter.decrypt("4444")))
