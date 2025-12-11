def bfs(grid, r, c):
    # performs bfs using the coordinate given by r and c 
    dirs = [[0,1], [0,-1], [1,0], [-1,0]]
    queue = [] # queue to store the sequence of neighboring nodes to visit 
    print(r,c)
    queue.append([r,c])

    while queue: 
        print("queue before popping: {}".format(queue))
        nr, nc = queue.pop(0)
        for dir in dirs: 
            print("nr nc before adding dir: {}, {}".format(nr, nc))
            # explore nodes in all 4 directions 
            nr = nr + dir[0]
            nc = nc + dir[1]
            print("nr, nc before adding to queue: {}, {}. dir[0], dir[1]: {}, {}".format(nr,nc,dir[0], dir[1]))


grid = [["1", "1"]]
bfs(grid,0,0)
