# Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

# Example 1:

# Input: "babad"
# Output: "bab"
# Note: "aba" is also a valid answer.
# Example 2:

# Input: "cbbd"
# Output: "bb"

class Solution:
    def longestPalindrome(self, s: str) -> str:
        # Return if string is empty of 1 letter
        if len(s) < 2:
            return s
        longestPal = ""
        
        for i in range(len(s)):
            j = i + 1
            # While j is less the length of string
            # and longest palindrome length is less or equal to substring s[i:]
            while j <= len(s) and len(longestPal) <= len(s[i:]):
                # if substring of s[i:j] is a palindrome
                # and substring is longer then longest palindrome so far
                if s[i:j] == s[i:j][::-1] and len(s[i:j]) > len(longestPal):
                    longestPal = s[i:j]
                j += 1
        return longestPal
    