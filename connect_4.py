################################################################################
#   Authors:                                                                   #
#       · Alejandro Santorum Varela - alejandro.santorum@estudiante.uam.es     #
#                                     alejandro.santorum@gmail.com             #
#   Date: Apr 14, 2019                                                         #
#   File: connect_4.py                                                         #
#   Project: Connect4 - Predicting heuristic values                            #
#   Version: 1.1                                                               #
################################################################################
import numpy as np
import math
import matplotlib.pyplot as plt
import seaborn as sns
import tkinter as tk
sns.set()

USER = 1
OPP  = -1
WALL = -2
COUNTED = 0
STOP_REASON = 1

class Board():

    def __init__(self, nrows , ncols):
        # Number of board rows
        self.nrows = nrows
        # Number of board columns
        self.ncols = ncols
        # Board is represented as a matrix
        self.board = np.zeros((nrows, ncols))
        # Array of heigths (number of pieces placed in each col)
        self.height = np.zeros(ncols)

    def print_board(self):
        print(self.board)
        print()

    def count_right(self , row , col , piece):
        sum = 0
        while col<(self.ncols-1):
            if (self.board[row][col] != piece):
                return sum, self.board[row][col]
            else:
                sum += 1
            col += 1
        return sum, WALL

    def count_left(self , row , col , piece):
        sum = 0
        while col>=0:
            if (self.board[row][col] != piece):
                return sum, self.board[row][col]
            else:
                sum += 1
            col -= 1
        return sum, WALL

    def count_up(self , row , col , piece):
        sum = 0
        while row>=0:
            if (self.board[row][col] != piece):
                return sum, self.board[row][col]
            else:
                sum += 1
            row -= 1
        return sum, WALL

    def count_down(self , row , col , piece):
        sum = 0
        while row<(self.nrows-1):
            if (self.board[row][col] != piece):
                return sum, self.board[row][col]
            else:
                sum += 1
            row += 1
        return sum, WALL

    def count_up_right(self , row , col , piece):
        sum = 0
        while ((row>=0) and (col<(self.ncols-1))):
            if (self.board[row][col] != piece):
                return sum, self.board[row][col]
            else:
                sum+=1
            row -= 1
            col += 1
        return sum, WALL

    def count_up_left(self , row , col , piece):
        sum = 0
        while ((row>=0) and (col>=0)):
            if (self.board[row][col] != piece):
                return sum, self.board[row][col]
            else:
                sum+=1
            row -= 1
            col -= 1
        return sum, WALL

    def count_down_right(self , row , col , piece):
        sum = 0
        while ((row<(self.nrows-1)) and (col<(self.ncols-1))):
            if (self.board[row][col] != piece):
                return sum, self.board[row][col]
            else:
                sum+=1
            row += 1
            col += 1
        return sum, WALL

    def count_down_left(self , row , col , piece):
        sum = 0
        while ((row<(self.nrows-1)) and (col>=0)):
            if (self.board[row][col] != piece):
                return sum, self.board[row][col]
            else:
                sum+=1
            row += 1
            col -= 1
        return sum, WALL

    def count_horizontal(self , row , col , piece):
        return (self.count_left(row , col , piece)[COUNTED] + self.count_right(row , col+1 , piece)[COUNTED])

    def count_vertical(self , row , col , piece):
        return (self.count_up(row , col , piece)[COUNTED] + self.count_down(row+1 , col , piece)[COUNTED])

    def count_diag_desc(self , row , col , piece):
        return (self.count_down_right(row , col ,piece )[COUNTED] + self.count_up_left(row -1 , col - 1 , piece)[COUNTED])

    def count_diag_asc(self, row , col , piece):
        return (self.count_up_right(row, col , piece)[COUNTED] + self.count_down_left(row + 1 , col - 1 , piece )[COUNTED])

    def winner(self , row , col , piece):
        if (self.count_horizontal(row , col , piece ) == 4):
            return piece
        if (self.count_vertical(row , col , piece ) == 4):
            return piece
        if (self.count_diag_asc(row, col , piece) == 4):
            return piece
        if (self.count_diag_desc(row , col , piece) == 4):
            return piece
        return 0

    ###############################################
    #   It inserts a piece in a given column
    #   User has to check the board status
    #   before inserting the piece, because
    #   this function does not check it
    ###############################################
    def insert(self , piece , col):
        counter = 0
        for i in range(self.nrows):
            counter += np.abs(self.board[i][col])
        pos = self.nrows - (counter+1)
        self.board[int(pos)][col] = piece
        self.height[col] += 1
        return int(pos)

    ###############################################
    #   It removes the last piece played in the
    #   provided column
    ###############################################
    def go_back(self, col):
        for i in range(self.nrows):
            if self.board[i][col] != 0:
                self.board[i][col] = 0
                return

    ###############################################
    #   It builds a board given a status pattern,
    #   truncating it if the pattern represents
    #   a winner status
    ###############################################
    def build_pattern(self, pattern):
        length = len(pattern)
        current_board = ""
        current_piece = 1
        for i in range(length):
            col_move = int(pattern[i])-1 # Pattern indexes in 1
            inserted_row = self.insert(current_piece, col_move)
            if self.winner(inserted_row, col_move, current_piece):
                self.go_back(col_move)
                return current_board, current_piece
            current_board += pattern[i]
            current_piece = 0-current_piece # Swaping player move
        return current_board, current_piece

    def _calculate_N_in_a_row(self, piece, N):
        blocked = 0
        effective = 0
        for i in range(self.nrows):
            for j in range(self.ncols):
                sum, obstacle = self.count_right(i, j, piece)
                if sum == N:
                    if obstacle == 0:
                        effective += 1
                    else:
                        blocked += 1
                sum, obstacle = self.count_left(i, j, piece)
                if sum == N:
                    if obstacle == 0:
                        effective += 1
                    else:
                        blocked += 1
                sum, obstacle = self.count_up(i, j, piece)
                if sum == N:
                    if obstacle == 0:
                        effective += 1
                    else:
                        blocked += 1
                sum, obstacle = self.count_down(i, j, piece)
                if sum == N:
                    if obstacle == 0:
                        effective += 1
                    else:
                        blocked += 1
                sum, obstacle = self.count_up_right(i, j, piece)
                if sum == N:
                    if obstacle == 0:
                        effective += 1
                    else:
                        blocked += 1
                sum, obstacle = self.count_up_left(i, j, piece)
                if sum == N:
                    if obstacle == 0:
                        effective += 1
                    else:
                        blocked += 1
                sum, obstacle = self.count_down_right(i, j, piece)
                if sum == N:
                    if obstacle == 0:
                        effective += 1
                    else:
                        blocked += 1
                sum, obstacle = self.count_down_left(i, j, piece)
                if sum == N:
                    if obstacle == 0:
                        effective += 1
                    else:
                        blocked += 1
        return blocked, effective

    def _mean_distance(self, piece):
        acum = 0.0
        counter = 0.0
        for i in range(self.nrows):
            for j in range(self.ncols):
                if self.board[i][j] == piece:
                    for k in range(self.nrows):
                        for l in range(self.ncols):
                            if self.board[k][l]==piece and (k!=i or l!=j):
                                # Euclidean norm
                                acum += math.sqrt(((i-k)**2)+((j-l)**2))
                                counter += 1.0
        return acum/counter

    def _frac_zone(self, piece, ini_col_ind, fin_col_ind):
        allied = 0
        enemy = 0
        i = ini_col_ind
        while i <= fin_col_ind:
            allied += self.count_vertical(0, i, piece)
            enemy += self.count_vertical(0, i, -piece)
            i += 1
        allied -= enemy
        return 5 + 0.5*allied

    def _vertical_groups_of_4(self, piece, n_pieces):
        counter = 0
        for i in range(self.ncols):
            for j in range(self.nrows-3): # -3 becuase it is connect 4
                aux = 0
                if (self.board[j][i] == -piece) or (self.board[j+1][i] == -piece) or \
                (self.board[j+2][i] == -piece) or (self.board[j+3][i] == -piece):
                    continue
                if self.board[j][i] == piece:
                    aux += 1
                if self.board[j+1][i] == piece:
                    aux += 1
                if self.board[j+2][i] == piece:
                    aux += 1
                if self.board[j+3][i] == piece:
                    aux += 1
                if aux == n_pieces:
                    counter += 1
        return counter

    def _horizontal_groups_of_4(self, piece, n_pieces):
        counter = 0
        for i in range(self.nrows):
            for j in range(self.ncols-3): # -3 becuase it is connect 4
                aux = 0
                if (self.board[i][j] == -piece) or (self.board[i][j+1] == -piece) or \
                (self.board[i][j+2] == -piece) or (self.board[i][j+3] == -piece):
                    continue
                if self.board[i][j] == piece:
                    aux += 1
                if self.board[i][j+1] == piece:
                    aux += 1
                if self.board[i][j+2] == piece:
                    aux += 1
                if self.board[i][j+3] == piece:
                    aux += 1
                if aux == n_pieces:
                    counter += 1
        return counter

    def _diagonal_ppal_groups_of_4(self, piece, n_pieces):
        counter = 0
        for i in range(self.ncols-3):
            for j in range(3, self.nrows): # 3 becuase it is connect 4
                aux = 0
                if (self.board[j][i] == -piece) or (self.board[j-1][i+1] == -piece) or \
                (self.board[j-2][i+2] == -piece) or (self.board[j-3][i+3] == -piece):
                    continue
                if self.board[j][i] == piece:
                    aux += 1
                if self.board[j-1][i+1] == piece:
                    aux += 1
                if self.board[j-2][i+2] == piece:
                    aux += 1
                if self.board[j-3][i+3] == piece:
                    aux += 1
                if aux == n_pieces:
                    counter += 1
        return counter

    def _diagonal_neg_groups_of_4(self, piece, n_pieces):
        counter = 0
        for i in range(self.ncols-3):
            for j in range(self.nrows-3): # 3 becuase it is connect 4
                aux = 0
                if (self.board[j][i] == -piece) or (self.board[j+1][i+1] == -piece) or \
                (self.board[j+2][i+2] == -piece) or (self.board[j+3][i+3] == -piece):
                    continue
                if self.board[j][i] == piece:
                    aux += 1
                if self.board[j+1][i+1] == piece:
                    aux += 1
                if self.board[j+2][i+2] == piece:
                    aux += 1
                if self.board[j+3][i+3] == piece:
                    aux += 1
                if aux == n_pieces:
                    counter += 1
        return counter


    def get_features(self, piece):
        features = []
        # Total number of pieces
        features.append(sum(self.height))
        # Ally mean distance
        features.append(self._mean_distance(piece))
        # Opponent mean distance
        features.append(self._mean_distance(-piece))
        # Ally #2-in-a-row
        block, eff = self._calculate_N_in_a_row(piece, 2)
        features.append(block)
        features.append(eff)
        # Opponent #2-in-a-row
        block, eff = self._calculate_N_in_a_row(-piece, 2)
        features.append(block)
        features.append(eff)
        # Ally #3-in-a-row
        block, eff = self._calculate_N_in_a_row(piece, 3)
        features.append(block)
        features.append(eff)
        # Opponent #3-in-a-row
        block, eff = self._calculate_N_in_a_row(-piece, 3)
        features.append(block)
        features.append(eff)
        return features


    def available_site(self, col):
        if (self.height[col]<6):
            return 1
        return 0

    def plot_configuration(self):
        fig = plt.figure(num=None, figsize=(12, 8), dpi=80, facecolor='w', edgecolor='k')
        plt.pcolormesh( self.board, cmap=plt.cm.RdBu);
        plt.axis('off')
        plt.title('Connect 4')
        plt.show(True)

    def evolve_game(self):
        print("Game Starting")
        win = 0
        turn = 0
        while win==0:
            if (turn%2==0):
                print("User insert a col $$$$---> ")
                col = int(input())-1
                if self.available_site(col):
                    self.insert(USER , col)
                    win = self.winner(6-int(self.height[col]) , col , USER)
                    #self.plot_configuration()
                    #test.print_board()
                    turn += 1
                else:
                    print("Incorrect Col")

            else:
                print("Opponent turn insert a col $$$$----> ")
                col = int(input())-1
                if self.available_site(col):
                    self.insert(OPP , col)
                    win = self.winner(6-int(self.height[col]) , col , OPP)
                    #self.plot_configuration()
                    #test.print_board()
                    turn += 1
                else:
                    print("Incorrect Col")

        print("Game finished")
        return


class gui():
    import tkinter as tk
    import PIL
    def __init__(self , master, cols , rows, board):
        self.master = master
        self.ncols = cols
        self.nrows = rows
        self.buttons = [[]]
        self.board = board
        self.red_piece = tk.PhotoImage(file = "images/roja.png")
        #self.blue_piece = tk.PhotoImage(file = "images/azul.jpg")
        for i in range(self.nrows):
            buttonRow = []
            for j in range(self.ncols):
                button = tk.Button(self.master,text="placeholder",width=100,height=100).grid(row=i,column=j)
                button.bind("<Button-1>",lambda: self.place_piece(piece,col))
                buttonRow.append(button)
            self.buttons.append(buttonRow)
    def rename_title(self):
        self.master.title("Connect 4")

    def change_pic(labelname):
        photo1 = ImageTk.PhotoImage(Image.open("images/roja.png"))
        labelname.configure(image=photo1)
        labelname.photo = photo1

    def place_piece(self,event,piece,col):
        if self.board.available_site(col):
            self.board.insert(piece,col)
            height = 6-int(self.board.height[col])
            self.buttons[height][col].config(image=self.red_piece,compound=tk.RIGHT)
        else:
            tk.messagebox.showinfo("Alert Message" , "This Column is already full")


    def define_labels(self):
        return 0


if __name__ == "__main__":
    nrows = 6
    ncols = 7
    ###################################################
    # TESTING BUILD_PATTERN AND GET FEATURES
    #board = Board(nrows, ncols)
    #board.build_pattern("1231241352463")
    #board.print_board()
    #board.testing_groups(1)

    ###################################################
    # TESTING GUI
    test = Board(nrows, ncols)
    test.evolve_game()
    windows = tk.Tk()
    windows.geometry("1200x1000")
    mainWIndow = gui(windows , 6 , 7,Board(6 , 7))
    windows.mainloop()
