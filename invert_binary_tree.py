# Invert a binary tree.
# Input:
#      4
#    /   \
#   2     7
#  / \   / \
# 1   3 6   9
#
# Output:
#      4
#    /   \
#   7     2
#  / \   / \
# 9   6 3   1

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Solution:

    def invertTree(self, node: TreeNode) -> TreeNode:
        if not node:
            return None
        
        node.left, node.right = self.invertTree(node.right), self.invertTree(node.left)

        return node
        