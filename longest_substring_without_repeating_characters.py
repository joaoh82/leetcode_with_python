# Given a string, find the length of the longest substring without repeating characters.

# Example 1:

# Input: "abcabcbb"
# Output: 3 
# Explanation: The answer is "abc", with the length of 3. 
# Example 2:

# Input: "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.
# Example 3:

# Input: "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3. 
#              Note that the answer must be a substring, "pwke" is a subsequence and not a substring.

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxCount = 0
        currentCount = 0
        charList = []
        
        i = 0
        while i < len(s):
            for j in range(i, len(s)):
                if s[j] not in charList:
                    charList.append(s[j])
                    currentCount += 1
                else:
                    if currentCount > maxCount:
                        maxCount = currentCount
                    currentCount = 0
                    charList = []
                    i += 1
                    break
        
        return maxCount