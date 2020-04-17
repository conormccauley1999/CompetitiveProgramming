vis = set()

def dfs(grid, x, y):
    if x < 0 or x >= len(grid[0]) or y < 0 or y >= len(grid):
        return
    if (x, y) in vis or grid[y][x] == '0':
        return
    vis.add((x, y))
    dfs(grid, x - 1, y)
    dfs(grid, x + 1, y)
    dfs(grid, x, y - 1)
    dfs(grid, x, y + 1)

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        global vis
        vis = set()
        cnt = 0
        for y in range(len(grid)):
            for x in range(len(grid[0])):
                if grid[y][x] != '1' or (x, y) in vis:
                    continue
                cnt += 1
                dfs(grid, x, y)
        return cnt
