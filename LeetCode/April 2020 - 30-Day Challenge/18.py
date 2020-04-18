INF = 10 ** 10
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        h, w = len(grid), len(grid[0])
        for y in range(h):
            for x in range(w):
                if x == 0 and y == 0:
                    continue
                u = INF if y == 0 else grid[y - 1][x]
                v = INF if x == 0 else grid[y][x - 1]
                grid[y][x] += min(u, v)
        return grid[h - 1][w - 1]
