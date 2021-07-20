import math

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.foo = 0

        def traverse(node: TreeNode, maxBound: int):
            if not node:
                return
            elif node.val >= maxBound:
                self.foo  += 1
            traverse(node.left, max(node.val, maxBound))
            traverse(node.right, max(node.val, maxBound))

        traverse(root, -math.inf)
        return self.foo


