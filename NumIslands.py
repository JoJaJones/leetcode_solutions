sink_dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]

class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        self.num_rows = len(grid)
        if self.num_rows > 0:
            self.num_cols = len(grid[0])
        else:
            return 0
        
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                cur = i, j
                if self.is_island(cur, grid):
                    self.sink_island(cur, grid)
                    count += 1

        return count
        
    def is_island(self, pos, grid):
        r, c = pos
        return grid[r][c] == '1'
    
    def sink_island(self, pos, grid):
        stack = [pos]
        self.sink_pos(pos, grid)
        while len(stack) > 0:
            cur = stack.pop()
            for direction in sink_dirs:
                next_pos = self.get_next_pos(cur, direction)
                if next_pos and self.is_island(next_pos, grid):
                    stack.append(next_pos)
                    self.sink_pos(next_pos, grid)
    
    def sink_pos(self, pos, grid):
        r, c = pos
        grid[r][c] = '0'
        
    
    def get_next_pos(self, pos, direction):
        r, c = pos
        d_r, d_c = direction
        next_pos = r + d_r, c + d_c
        if self.is_valid(next_pos):
            return next_pos
        
        return None
    
    def is_valid(self, pos):
        r, c = pos
        return 0 <= r < self.num_rows and 0 <= c < self.num_cols
