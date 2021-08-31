# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Result:
    def __init__(self, maybeOne, lca):
        self.maybeOne = maybeOne
        self.lca = lca
        if lca:
            self.maybeOne = None
            self.lca = lca

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        def traverse(curr, left, right):
            if not curr:
                return Result(None, None)
            else:
                leftResult = traverse(curr.left, left, right)
                maybeLeft, maybeLeftLCA = leftResult.maybeOne, leftResult.lca
                rightResult = traverse(curr.right, left, right)
                maybeRight, maybeRightLCA = rightResult.maybeOne, rightResult.lca
                if maybeLeftLCA:
                    return Result(None, maybeLeftLCA)
                elif maybeRightLCA:
                    return Result(None, maybeRightLCA)
                elif maybeLeft and maybeRight:
                    return Result(None, curr)
                elif maybeLeft or maybeRight:
                    if curr == left or curr == right:
                        return Result(None, curr)
                    else:
                        return Result(maybeLeft if maybeLeft else maybeRight, None)
                elif curr == left or curr == right:
                    return Result(curr, None)
                else:
                    return Result(None, None)

        result = traverse(root, p, q)
        return result.lca