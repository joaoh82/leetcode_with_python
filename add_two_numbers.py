# You are given two non-empty linked lists representing two non-negative integers. 
# The digits are stored in reverse order and each of their nodes contain a single digit. 
# Add the two numbers and return it as a linked list.

# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

# Example:
# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8
# Explanation: 342 + 465 = 807.

# Definition for singly-linked list.

class ListNode:
    def __init__(self, x, nextNode=None):
        self.val = x
        self.next = nextNode

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        firstNum = []
        secondNum = []
        
        currentL1 = l1
        while currentL1 is not None:
            firstNum.insert(0,currentL1.val)
            currentL1 = currentL1.next
        currentL2 = l2
        while currentL2 is not None:
            secondNum.insert(0,currentL2.val)
            currentL2 = currentL2.next
        
        twoNumberSum = self.magicHelper(firstNum) + self.magicHelper(secondNum)
        
        result = list(reversed([int(x) for x in str(twoNumberSum)]))
        resultNode = self.listToLinkedList(result)
        
        return resultNode
    
    def listToLinkedList(self, lst):
        assert len(lst) > 0
        if len(lst) == 1:
            return ListNode(lst[0])
        else:
            return ListNode(lst[0], self.listToLinkedList(lst[1:]))
            
    def magicHelper(self, numbers) -> int:
        s = ''.join(map(str, numbers))
        return int(s)