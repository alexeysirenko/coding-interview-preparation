# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import defaultdict

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        graph = defaultdict(lambda: set())

        def buildGraph(curr, prev):
            if not curr:
                return
            if prev:
                graph[prev].add(curr)
                graph[curr].add(prev)
            buildGraph(curr.left, curr)
            buildGraph(curr.right, curr)

        buildGraph(root, None)

        results = []
        visited = set()
        def findKDistanceToTarget(node, k):
            if not node or node in visited:
                return
            visited.add(node)
            if k == 0:
                results.append(node.val)
                return
            else:
                for neigh in graph[node]:
                    findKDistanceToTarget(neigh, k - 1)

        findKDistanceToTarget(target, k)
        return results




