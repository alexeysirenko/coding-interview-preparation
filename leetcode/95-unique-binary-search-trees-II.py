# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:

        def traverse(leftNum, rightNum):
            if leftNum > rightNum:
                return [None]
            if leftNum == rightNum:
                return [TreeNode(leftNum)]
            results = []
            for rootNum in range(leftNum, rightNum + 1):
                allLeftNodes = traverse(leftNum, rootNum - 1)
                allRightNodes = traverse(rootNum + 1, rightNum)
                for leftNode in allLeftNodes:
                    for rightNode in allRightNodes:
                        rootNode = TreeNode(rootNum)
                        rootNode.left = leftNode
                        rootNode.right = rightNode
                        results.append(rootNode)
            return results

        return traverse(1, n)