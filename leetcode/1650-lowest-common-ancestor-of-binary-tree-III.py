"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        visited = set()

        def visit(node):
            if node:
                visited.add(node)

        while p or q:
            if p == q:
                return p
            if p in visited:
                return p
            if q in visited:
                return q
            visit(p)
            visit(q)
            p = p.parent if p else None
            q = q.parent if q else None


