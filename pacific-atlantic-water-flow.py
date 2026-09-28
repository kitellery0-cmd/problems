# here we work from out to in, marking valid cells for each seen, then running
# through and finding matches for both oceans.

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])
        pacific, atlantic = set(), set()
        directions = ((0, 1), (0, -1), (1, 0), (-1, 0))
        res = []

        def dfs(seen, prev_height, row, col):
            if ((row, col) in seen or min(row, col) < 0 or
                row >= rows or col >= cols or heights[row][col] < prev_height):
                return
            seen.add((row, col))
            for rc, cc in directions: # check each adjacent cell
                dfs(seen, heights[row][col], row + cc, col + rc)
                
        # propogate each seen
        def fill_ocean(ocean, row_side, col_side):
            for row in range(rows):
                dfs(ocean, heights[row][col_side], row, col_side)
            for col in range(cols):
                dfs(ocean, heights[row_side][col], row_side, col)

        fill_ocean(pacific, 0, 0)
        fill_ocean(atlantic, rows - 1, cols - 1) 
        
        for row in range(rows): # check for hits
            for col in range(cols):
                if (row, col) in pacific and (row, col) in atlantic:
                    res.append([row, col])
        return res







        # original propogation method below ---------------
    
        # # propogate the sets
        # for row in range(rows):   # left / right
        #     dfs(row, 0, pacific, heights[row][0])
        #     dfs(row, cols - 1, atlantic, heights[row][cols - 1])
            
        # for col in range(cols):   # top / bottom
        #     dfs(0, col, pacific, heights[0][col])
        #     dfs(rows - 1, col, atlantic, heights[rows - 1][col])
