# This program should solve a sudoku board using backtracking
# To solve this recursively think of how to solve one case, after making a valid choice i will simply call the function again but with the next choice in focus

# Rules:
# 1 of each number per row
# 1 of each number per column
# 1 of each number per 6 number subgrid

# board = [[9,0,3,0,0,0,5,0,1],
#         [0,0,0,3,0,0,0,0,0],
#         [0,0,0,7,0,1,0,0,2],
#         [6,0,0,0,0,0,0,0,0],
#         [0,8,0,0,6,0,9,1,0],
#         [0,0,0,0,2,4,0,7,0],
#         [3,0,9,2,0,0,6,5,0],
#         [5,0,0,0,9,0,0,0,0],
#         [0,0,1,0,0,0,7,0,0]]


# check if option is a valid choice

def validateChoice(board, r, n, option):

    # board is the current sudoku board
    # r is the index of the row containing the option being checked within the board
    # n is the index of the number being checked within the board
    # option is the value being validated

    # Check if the option exists on that row
    for b in range(len(board[r])):
        if board[r][b] == option and b!=n:
            return False
        
    # iterate through indexes of board rows o = 0->8
    # board[o] is then the row in focus
    for o in range(len(board)):

        # check if option exists on that column
        if board[o][n] == option and o!=r:
            return False
        
        # nested for loops through 0 to 8 for every row, used for looping through positions
        # i is the index of the position currently in focus i=0->8
        for i in range(9):

            # the way to know if 2 positions are in the same subgroup is whether the result of their index//3 is the same
            # numbers in positions 0,1,2 all return 0. positions 3,4,5 all contain one 3. 6,7,8 all contain two 3s.
            if i//3==n//3 and o//3==r//3:
                if option==board[o][i] and (o!=r or i!=n):
                    return False
                
    return True
        
    
# main function
# sudoku squares have numbers f from 0-80

def SudokuSolver(f=0):
    print(f)
    global board

    r = f//9
    n = f%9


    if f>=len(board[0])*len(board):
        print("return 1")
        return True

    if board[r][n]!=0:
        if SudokuSolver(f+1):
            print("return 2-True")
            return True
        else:
            print("return 2-False")
            return False

    for option in range(1,10):
        print("checking "+str(option))
        if validateChoice(board,r,n,option):
            board[r][n]=option
            if SudokuSolver(f+1)==True:
                print("return 3")
                return True
            else:
                print("following choice returned nvc, so continuing")
                # reset position after no valid choice on following square. otherwise if no other number is found and we unwind a layer, this position's current choice will affect that layer's choice
                board[r][n]=0
                continue

    # return false means this call for this position has nvc
    print("no valid choice at position "+str(r),str(n))
    print("return 4")
    return False


board=[]
rowww=[]
for xx in range(9):
        for yy in range(9):
            rowww.append(int(input("Position "+str(xx)+","+str(yy)+": ")))
        board.append(rowww)
        rowww=[]

SudokuSolver()
for line in board:
    print(line)
