

def count_trees(n):
  memo = {}

  def traverse(fromIdx, toIdx):
    if fromIdx >= toIdx:
      return 1
    else:
      currLen = toIdx - fromIdx
      if currLen in memo:
        return memo[currLen]
      count = 0
      for rootIdx in range(fromIdx, toIdx + 1):
        nLeft = traverse(fromIdx, rootIdx - 1)
        nRight = traverse(rootIdx + 1, toIdx)
        count += nLeft * nRight
      memo[currLen] = count
      return count

  return traverse(0, n - 1)


def main():
  print("Total trees: " + str(count_trees(2)))
  print("Total trees: " + str(count_trees(3)))


main()
