class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        direction = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        m = len(grid)
        n = len(grid[0])
        perimeter = 0
        for i in range(m):
            for j in range(n):
                for d in direction:
                    if grid[i][j] == 0:
                        continue
                    if self.beyond(i + d[0], j + d[1], m, n):
                        perimeter += 1
                    else:
                        if grid[i + d[0]][j + d[1]] == 0:
                            perimeter += 1
        return perimeter
    
    def beyond(self, i, j, m, n):
        if i < 0 or j < 0 or i >= m or j >= n:
            return True
        return False
