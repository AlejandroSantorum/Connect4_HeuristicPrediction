import numpy as np


user = 1
opp  = -1

class Board():
    def __init__(self, nrows , ncols):
        self.nrows = nrows
        self.ncols = ncols
        self.board = np.zeros((nrows, ncols))
        self.height = np.zeros(7)

    def print_board(self):
        print(self.board)
        print()

    def count_right(self , row , col , ficha):
        sum = 0
        while col<self.ncols:
            if (self.board[row][col] == (-ficha) or (self.board[row][col] == 0)):
                return sum
            else:
                sum += 1
            col += 1
        return sum

    def count_left(self , row , col , ficha):
        sum = 0
        while col>=0:
            if (self.board[row][col] == (-ficha) or (self.board[row][col] == 0)):
                return sum
            else:
                sum += 1
            col -= 1
        return sum

    def count_up(self , row , col , ficha):
        sum = 0
        while row>=0:
            if (self.board[row][col] == (-ficha) or (self.board[row][col] == 0)):
                return sum
            else:
                sum += 1
            row -= 1
        return sum

    def count_down(self , row , col , ficha):
        sum = 0
        while row<6:
            if (self.board[row][col] == (-ficha) or (self.board[row][col] == 0)):
                return sum
            else:
                sum += 1
            row += 1
        return sum

    def count_up_right(self , row , col , ficha):
        sum = 0
        while ((row>=0) or (col<self.ncols)):
            if (self.board[row][col] == (-ficha) or (self.board[row][col] ==0)):
                return sum
            else:
                sum+=1
            row -= 1
            col += 1
        return sum

    def count_up_left(self , row , col , ficha):
        sum = 0
        while ((row>=0) or (col>=0)):
            if (self.board[row][col] == (-ficha) or (self.board[row][col] ==0)):
                return sum
            else:
                sum+=1
            row -= 1
            col -= 1
        return sum

    def count_down_right(self , row , col , ficha):
        sum = 0
        while ((row<self.nrows) or (col<self.ncols)):
            if (self.board[row][col] == (-ficha) or (self.board[row][col] ==0)):
                return sum
            else:
                sum+=1
            row += 1
            col += 1
        return sum

    def count_down_left(self , row , col , ficha):
        sum = 0
        while ((row<self.nrows) or (col>=0)):
            if (self.board[row][col] == (-ficha) or (self.board[row][col] ==0)):
                return sum
            else:
                sum+=1
            row += 1
            col -= 1
        return sum

    def count_horizontal(self , row , col , ficha):
        return (self.count_left(row , col , ficha) + self.count_right(row , col+1 , ficha))

    def count_vertical(self , row , col , ficha):
        return (self.count_up(row , col , ficha) + self.count_down(row+1 , col , ficha))

    def count_diag_desc(self , row , col , ficha):
        return (self.count_down_right(row , col ,ficha ) + self.count_up_left(row -1 , col - 1 , ficha) )

    def count_diag_asc(self, row , col , ficha):
        return (self.count_up_right(row, col , ficha) + self.count_down_left(row + 1 , col - 1 , ficha ))


    def winner(self , row , col , ficha):
        if (self.count_horizontal(row , col , ficha ) == 4):
            print("Winner :: " , ficha )
            return ficha
        if (self.count_vertical(row , col , ficha ) == 4):
            print("Winner:: " , ficha )
            return ficha
        if (self.count_diag_asc(row, col , ficha))==4:
            print("Winner:: " , ficha )
            return ficha
        if (self.count_diag_desc(row , col , ficha))==4:
            print("Winner:: " , ficha)
            return ficha
        return 0

    def insert(self , ficha , col):
        #check before inserting a new ficha
        counter = 0
        for i in range(self.nrows):
            counter += np.abs(self.board[i][col])
        pos = 6 - (counter+1)
        self.board[int(pos)][col] = ficha
        self.height[col] += 1

    def available_site(self, col):
        if (0 in self.board[col]):
            return 1
        return 0


if __name__ == "__main__":
    test = Board(6,7)

    test.insert(user , 2)
    test.print_board()
    test.insert(opp,2)
    test.print_board()
    test.insert(user , 2 )
    test.print_board()
    test.insert(opp , 2)
    test.print_board()
    test.insert(user , 4)
    test.print_board()
    test.insert(opp , 6)
    test.print_board()
    test.insert(user , 3)
    test.print_board()
    print("Right: " , test.count_right(-1, 2, user))
    print("Left : " , test.count_left(-1, 4, user))
    print("Up: " , test.count_up(5 , 2, user))
    print("Down : " , test.count_down( -1 , 2, user))
    test.insert(opp , 2)
    test.print_board()
    test.insert(opp,2)
    test.print_board()
    test.insert(opp , 2 )
    test.print_board()
    test.insert(opp , 2)
    test.print_board()
    test.insert(user , 4)
    test.print_board()
    test.insert(opp , 6)
    test.print_board()
    test.insert(user , 3)
    test.print_board()
    print("Right: " , test.count_right(-1, 2, user))
    print("Left : " , test.count_left(-1, 4, user))
    print("Up: " , test.count_up(2 , 2, opp))
    print("Down : " , test.count_down(0 , 2, opp))
    print("Right down: " , test.count_down_right(-2, 3, user))
    print("Left down: " , test.count_down_left(-2, 4, user))
    print("Up right : " , test.count_up_right(-1, 3, user))
    print("Up left : " , test.count_up_left(-1 , 3, user))
    print()
    print("Horizontal " , test.count_horizontal(-1 , 4 , user))
    print("Vertical  " , test.count_vertical(-1, 2 , opp))
    print("Ascentdet " , test.count_diag_asc(-1, 3 , user))
    print("Descente " , test.count_diag_desc(-2 , 3 , user))






class Node():
#monte carlo search tree

    def __init__(self , state , parent = None):
        self.visits = 1
        self.reward = 0.0
        self.children = []
