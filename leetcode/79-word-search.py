class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        height = len(board)
        width = len(board[0])

        def traverse(h, w, charIdx: int, usedCells):
            if h < 0 or w < 0 or h >= height or w >= width:
                return False
            if (h, w) in usedCells:
                return False
            if board[h][w] != word[charIdx]:
                return False
            if charIdx == len(word) - 1:
                return True
            usedCells = usedCells.copy()
            usedCells.add((h, w))
            charIdx += 1
            return traverse(h - 1, w, charIdx, usedCells) or traverse(h + 1, w, charIdx, usedCells) or traverse(h, w - 1, charIdx, usedCells) or traverse(h, w + 1, charIdx, usedCells)

        for h in range(height):
            for w in range(width):
                if traverse(h, w, 0, set()):
                    return True

        return False
