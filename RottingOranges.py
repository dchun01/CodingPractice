class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        count = 0
        bfs = deque([])

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    bfs.append((i,j,0))

        while bfs:
            i,j,count = bfs.popleft()

            if i-1 >= 0 and grid[i-1][j] == 1:
                grid[i-1][j] = 2
                bfs.append((i-1,j,count+1))
            
            if i+1 < len(grid) and grid[i+1][j] == 1:
                grid[i+1][j] = 2
                bfs.append((i+1,j,count+1))

            if j-1 >= 0 and grid[i][j-1] == 1:
                grid[i][j-1] = 2
                bfs.append((i,j-1,count+1))

            if j+1 < len(grid[0]) and grid[i][j+1] == 1:
                grid[i][j+1] = 2
                bfs.append((i,j+1,count+1))

        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    return -1

        return count