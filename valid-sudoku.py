class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        squares = defaultdict(set)

        for i in range(9):
            for j in range(9):
                x, y = (i // 3), (j // 3)
                cell = board[i][j]
                if (cell != '.') and (cell in rows[j] or 
                    cell in cols[i] or 
                    cell in squares[(x, y)]):
                    return False
                else:
                    rows[j].add(cell)
                    cols[i].add(cell)
                    squares[(x, y)].add(cell)
        return True
