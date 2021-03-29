
class TreeNode:
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None

def find_unique_trees(n):

  def traverse(fromNum, toNum):
    if fromNum > toNum:
      return [None]
    elif fromNum == toNum:
      return [TreeNode(fromNum)]
    else:
      results = []
      for rootNum in range(fromNum, toNum + 1):
        leftNodes = traverse(fromNum, rootNum - 1)
        rightNodes = traverse(rootNum + 1, toNum)
        for leftNode in leftNodes:
          for rightNode in rightNodes:
            rootNode = TreeNode(rootNum)
            rootNode.left = leftNode
            rootNode.righ = rightNode
            results.append(rootNode)

      return results

  # TODO: Write your code here
  return traverse(1, n)


def main():
  print("Total trees: " + str(len(find_unique_trees(2))))
  print("Total trees: " + str(len(find_unique_trees(3))))


main()
