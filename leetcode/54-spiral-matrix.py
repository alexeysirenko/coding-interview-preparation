class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        nRows = len(matrix)
        nCols = len(matrix[0])
        leftB, rightB, topB, bottomB = -1, nCols, -1, nRows

        ROW = 0
        COL = 1
        result = []
        goRight = [0, 1] # +row, +col
        goBottom = [1, 0]
        goLeft = [0, -1]
        goTop = [-1, 0]
        directionsInOrder = [goRight, goBottom, goLeft, goTop]

        def nextDirection(currDir):
            i = directionsInOrder.index(currDir)
            return directionsInOrder[i + 1] if i < len(directionsInOrder) - 1 else directionsInOrder[0]


        def adjustBounds(direction, leftB, rightB, topB, bottomB):
            if direction == goRight:
                topB += 1
            elif direction == goBottom:
                rightB -=1
            elif direction == goLeft:
                bottomB -= 1
            else:
                leftB += 1
            return (leftB, rightB, topB, bottomB)

        def canMove(nextRow, nextCol):
            return nextRow in range(topB + 1, bottomB) and nextCol in range(leftB + 1, rightB)

        currCol, currRow = 0, 0
        direction = directionsInOrder[0]
        while canMove(currRow, currCol):
            result.append(matrix[currRow][currCol])

            nextRow = currRow + direction[ROW]
            nextCol = currCol + direction[COL]

            if not canMove(nextRow, nextCol):
                leftB, rightB, topB, bottomB = adjustBounds(direction, leftB, rightB, topB, bottomB)
                direction = nextDirection(direction)
                currRow = currRow + direction[ROW]
                currCol = currCol + direction[COL]
            else:
                currRow = nextRow
                currCol = nextCol


        return result









