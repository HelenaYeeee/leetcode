# sol 1. use a set to store the location that should be crushed 
# debugging trick: when debugging for while loop, 
# 1. print out the variable in while condition 
# 2. limit loop to a for loop, e.g. for i in range(3) and see how it behaves 
class Solution:
    def candyCrush(self, board: List[List[int]]) -> List[List[int]]:
        
        m = len(board) # number of rows
        n = len(board[0]) # number of col

        def find():
            # find all candies that can be crushed and use a set to store its location 

            crushed_set = set()

            # find vertically adjacent candies
            for r in range(1, m-1):
                for c in range(n):
                    # my mistake: forgot to add the condition that current element must not be 0, causing 0 to be treated as candy instead of empty space
                    if board[r][c] == board[r-1][c] == board[r+1][c] and board[r][c] != 0:  
                        crushed_set.add((r,c))
                        crushed_set.add((r-1,c))
                        crushed_set.add((r+1,c))
            
            # next, find horizontally adjacent candies 
            for r in range(m):
                for c in range(1,n-1):
                    # my mistake: forgot to add the condition that current element must not be 0, causing 0 to be treated as candy instead of empty space
                    if board[r][c] == board[r][c-1] == board[r][c+1] and board[r][c] != 0:
                        crushed_set.add((r,c))
                        crushed_set.add((r,c-1))
                        crushed_set.add((r,c+1))

            return crushed_set                        

            

        def crush(crushed_set): 
            # for all candies marked in crushed_set, 
            # set them to 0 to indicate the location is now empty
            for i in crushed_set:
                board[i[0]][i[1]] = 0

            

        

        def drop(): 
            # simluate gravity, 
            # candies that remains will drop until they hit a candy or bottom
            

            for c in range(n):
                # for each col, traverse from bottom to top, 
                # swap any non-zero elements with the lowest zero 
                lowest_zero = -1
                for r in range(m-1,-1,-1):
                    
                    if board[r][c] == 0: 
                        lowest_zero = max(lowest_zero, r)
                    
                    elif board[r][c] != 0 and lowest_zero >= 0: # lowest_zero >= 0 or lowest_zero != -1 both works 
                        board[r][c], board[lowest_zero][c] = board[lowest_zero][c], board[r][c]
                        lowest_zero -= 1
        



        
        
        # main function here
        crushed_set = find()

        while crushed_set:

            crush(crushed_set)
        
            drop()
            crushed_set = find()
            print(crushed_set)
        
        return board


# sol 2. more optimized, but I don't expect you to think of it during interview 
# instead of using a set to store the location that should be crushed,
# we can flag candies to be crushed by -1 * candy value and compare the absolute value 
# This way, we modify values in place to optimize space complexity from O(m*n) -> O(1)
class Solution:
    def candyCrush(self, board: List[List[int]]) -> List[List[int]]:
        m = len(board) # number of rows
        n = len(board[0]) # number of col

        def find():
            # returns boolean to identify whether there's more candies to be crushed 
            complete = True 

            # find vertically adjacent nodes 
            for r in range(1,m-1):
                for c in range(n):
                    if abs(board[r][c]) == abs(board[r-1][c]) == abs(board[r+1][c]) and board[r][c] != 0: 
                        board[r][c] = -1 * abs(board[r][c])
                        board[r-1][c] = -1 * abs(board[r-1][c])
                        board[r+1][c] = -1 * abs(board[r+1][c])
                        complete = False
            
            # find horizontally adjacent nodes 
            for r in range(m):
                for c in range(1,n-1):
                    if abs(board[r][c]) == abs(board[r][c-1]) == abs(board[r][c+1]) and board[r][c] != 0: 
                        board[r][c] = -1 * abs(board[r][c])
                        board[r][c-1] = -1 * abs(board[r][c-1])
                        board[r][c+1] = -1 * abs(board[r][c+1])
                        complete = False
            return complete
            
        def crush(): 
            for r in range(m):
                for c in range(n):
                    if board[r][c] < 0:
                        board[r][c] = 0

        

        def drop(): 
            # simluate gravity, 
            # candies that remains will drop until they hit a candy or bottom
            

            for c in range(n):
                # for each col, traverse from bottom to top, 
                # swap any non-zero elements with the lowest zero 
                lowest_zero = -1
                for r in range(m-1,-1,-1):
                    
                    if board[r][c] == 0: 
                        lowest_zero = max(lowest_zero, r)
                    
                    elif board[r][c] != 0 and lowest_zero != -1: 
                        board[r][c], board[lowest_zero][c] = board[lowest_zero][c], board[r][c]
                        lowest_zero -= 1
        



        
        
        # main function here
        complete = find()

        while not complete:
            crush()
            drop()
            complete = find()
        
        return board
        