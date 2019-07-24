# Given an array of integers nums and an int k. Return the product of every k consecutive numbers.
# Example:
# Input: nums = [1, 3, 3, 6, 5, 7, 0, -3], k = 3
# Output: [1, 3, 9, 54, 90, 210, 0, 0]
# Explanation: 1 (1), 3 (1x3), 9 (1x3x3), 54 (3x3x6), 90 (3x6x5), 210 (6x5x7), 0 (5x7x0), 0 (7x0x-3)

# https://leetcode.com/discuss/interview-question/336746/google-onsite-product-of-k-consecutive-numbers

def solution(arr, k):
    size = len(arr)
    result = []
    for i in range(size):
        limit = i - k
        product = 1
        if i - k < 1:
            limit = -1
        for j in range(i, limit, -1):
            product *= arr[j]
        result.append(product)
    return result


print(solution([1, 3, 3, 6, 5, 7, 0, -3], 3))