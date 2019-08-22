# Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

# Note:

# The solution set must not contain duplicate triplets.

# Example:

# Given array nums = [-1, 0, 1, 2, -1, -4],

# A solution set is:
# [
#   [-1, 0, 1],
#   [-1, -1, 2]
# ]

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        triplets = []
        
        for i in range(len(nums)-2):
            if i > 0 and nums[i] == nums[i-1]: 
                continue
            leftIdx = i+1
            rightIdx = len(nums)-1
            while leftIdx < rightIdx:
                currentSum = nums[i] + nums[leftIdx] + nums[rightIdx]
                if currentSum < 0:
                    leftIdx += 1
                elif currentSum > 0:
                    rightIdx -= 1
                else:
                    triplets.append((nums[i], nums[leftIdx], nums[rightIdx]))
                    while leftIdx < rightIdx and nums[leftIdx] == nums[leftIdx + 1]: 
                        leftIdx += 1
                    while leftIdx < rightIdx and nums[rightIdx] == nums[rightIdx - 1]: 
                        rightIdx -= 1
                    leftIdx += 1
                    rightIdx -= 1
        return triplets