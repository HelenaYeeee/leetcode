# sol 1: use dfs 
class Solution:


    def numIslands(self, grid: List[List[str]]) -> int:
        # DFS 

        if not grid: 
            return 0
        row_length = len(grid)
        col_length = len(grid[0])
        count_island = 0

        for r in range(row_length):
            for c in range(col_length):
                if grid[r][c] == "1": 
                    # we found a new island because we found a root node that initiates a DFS 
                    count_island += 1
                    # pass the coordinate of root node to dfs 
                    self.dfs(grid, r, c)
        return count_island
    
    def dfs(self, grid, r, c):
        # performs dfs using the coordinate given by r and c 

        # base case
        # when r or c is out of index range, 
        # or when grid is not marked as 1 (meaning that it is either visited or is water)
        if (r < 0 or r > len(grid)-1 or c < 0 or c > len(grid[0])-1 or grid[r][c] != "1"):
            return
        
        # mark all visited node as 0 
        grid[r][c] = "0"
        dirs = [[0,1], [0,-1], [1,0], [-1,0]]
        for dir in dirs: 
            self.dfs(grid, r+dir[0], c+dir[1])



# sol 2: bfs 
class Solution:


    def numIslands(self, grid: List[List[str]]) -> int:
        # BFS

        if not grid: 
            return 0
        row_length = len(grid)
        col_length = len(grid[0])
        count_island = 0

        for r in range(row_length):
            for c in range(col_length):
                if grid[r][c] == "1": 
                    # we found a new island because we found a root node that initiates a DFS 
                    count_island += 1
                    grid[r][c] = "0"
                    # pass the coordinate of root node to bfs
                    self.bfs(grid, r, c)
        return count_island
    
    def bfs(self, grid, r, c):
        # performs bfs using the coordinate given by r and c 
        dirs = [[0,1], [0,-1], [1,0], [-1,0]]
        queue = [] # queue to store the sequence of neighboring nodes to visit 
        print(r,c)
        queue.append([r,c])

        while queue: 
            nr, nc = queue.pop(0)
            for dir in dirs: 
                # explore nodes in all 4 directions 
                nr_neighbour = nr + dir[0]
                nc_neighbour = nc + dir[1]

                if nr_neighbour >= 0 and nr_neighbour < len(grid) and nc_neighbour >= 0 and nc_neighbour < len(grid[0]) and grid[nr_neighbour][nc_neighbour] == "1":
                    # mark node as 0 to indicate that it is visited 
                    grid[nr_neighbour][nc_neighbour] = "0"
                    queue.append([nr_neighbour,nc_neighbour])


            
