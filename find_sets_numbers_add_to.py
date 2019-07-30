# Given an array, find 2 numbers that add to another given number


def add_numbers_to(arr, sum):
    leftIdx = 0
    rightIdx = len(arr)-1
    arr.sort()
    while leftIdx < rightIdx:
        if arr[leftIdx] + arr[rightIdx] == sum:
            return [arr[leftIdx], arr[rightIdx]]
        elif arr[leftIdx] + arr[rightIdx] < sum:
            leftIdx += 1
        elif arr[leftIdx] + arr[rightIdx] > sum:
            rightIdx -= 1
    return []

print(add_numbers_to([5, 7, 12, 54, 32], 18)) # []
print(add_numbers_to([5, 7, 12, 54, 32], 19)) # [7, 12]
print(add_numbers_to([5, 7, 12, 54, 32], 10)) # []
print(add_numbers_to([5, 7, 12, 54, 32], 37)) # [5, 32]
