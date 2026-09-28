class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        directions = ((0, 1), (1, 0), (0, -1), (-1, 0)) # right, down, left, up
        steps_remaining = [len(matrix[0]), len(matrix) - 1] # cols, rows

        r, c = 0, -1
        d = axis = 0

        while steps_remaining[axis]:
            rc, cc = directions[d]
            for _ in range(steps_remaining[axis]):
                r += rc
                c += cc
                res.append(matrix[r][c])
            steps_remaining[axis] -= 1
            d += 1
            d %= 4
            axis = d & 1
        return res

    
