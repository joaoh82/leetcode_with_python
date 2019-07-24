# Normal palindrome is defined as a string that reads the same backwards as forwards, for example "abccba".
# Chunked palindrome is defined as a string that you can split into chunks and it will form a palindrome.
# For example, "volvo". You can split it into (vo)(l)(vo). Let A = "vo", B = "l", so the original string is ABA which is a palindrome.

# Given a string str, find the maximum number of chunks we can split that string to get a chuncked palindrome.

# https://leetcode.com/discuss/interview-question/337515/Google-or-Onsite-or-Chunked-Palindrome

def solution(str):
    size = len(str)
    
    if not str:
        return 0
    
    for i in range(size//2):
        if str[:i+1] == str[size - 1 - i:]:
            return 2 + solution(str[i + 1: size - 1 - i])
    return 1
        

print(solution("valve"))
print(solution("voabcvo"))
print(solution("vovo"))
print(solution("volvolvo"))
print(solution("volvol"))
print(solution("aaaaaa"))