from collections import deque
from typing import List

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def bfs(x, y):
            queue = deque()
            queue.append((x, y))

            grid[x][y] = 0
            count = 1

            while queue:
                x, y = queue.popleft()

                for i in range(4):
                    nx = dx[i] + x
                    ny = dy[i] + y

                    if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]) and grid[nx][ny] == 1:
                        grid[nx][ny] = 0
                        count += 1
                        queue.append((nx, ny))

            return count

        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]
        max_area = 0

        for i in range(0, len(grid)):
            for j in range(0, len(grid[0])):
                if grid[i][j] == 1:
                    area = bfs(i, j)
                    max_area = max(max_area, area)

        return max_area