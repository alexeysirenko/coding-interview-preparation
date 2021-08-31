# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def traverse(leftNode, rightNode) -> bool:
            if not leftNode and not rightNode:
                return True
            if not leftNode or not rightNode:
                return False
            return leftNode.val == rightNode.val and traverse(leftNode.left, rightNode.right) and traverse(leftNode.right, rightNode.left)

        if not root:
            return False
        return traverse(root.left, root.right)



