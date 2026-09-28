class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        directions = ((0, 1), (0, -1), (1, 0), (-1, 0))
        rows = len(grid)
        cols = len(grid[0])

        def find_island(r, c):
            if ((r, c) in visited or min(r, c) < 0 or
                r >= rows or c >= cols or grid[r][c] == '0'):
                return False
            visited.add((r, c))
            for rc, cc in directions:
                find_island(r + rc, c + cc)
            return True
            

        islands = 0
        for r in range(rows):
            for c in range(cols):
                if find_island(r, c):
                    islands += 1
        return islands
