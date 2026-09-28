class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0])
        seen = set() # coords
        directions = ((0, 1), (0, -1), (1, 0), (-1, 0))

        def find_word(r, c, i):
            if i == len(word):
                return True
            elif (min(r, c) < 0 or c >= cols or r >= rows or
                board[r][c] != word[i] or (r, c) in seen):
                return False
            
            seen.add((r, c))
            for rc, cc in directions:
                if find_word(r + rc, c + cc, i + 1):
                    return True
            seen.remove((r, c))
            return False

        for r in range(rows):
            for c in range(cols):
                if find_word(r, c, 0):
                    return True
        return False
