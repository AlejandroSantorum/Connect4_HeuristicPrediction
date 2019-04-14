import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import tkinter as tk
sns.set()

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
        while col<(self.ncols-1):
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
        while row<(self.nrows-1):
            if (self.board[row][col] == (-ficha) or (self.board[row][col] == 0)):
                return sum
            else:
                sum += 1
            row += 1
        return sum

    def count_up_right(self , row , col , ficha):
        sum = 0
        while ((row>=0) and (col<(self.ncols-1))):
            if (self.board[row][col] == (-ficha) or (self.board[row][col] ==0)):
                return sum
            else:
                sum+=1
            row -= 1
            col += 1
        return sum

    def count_up_left(self , row , col , ficha):
        sum = 0
        while ((row>=0) and (col>=0)):
            if (self.board[row][col] == (-ficha) or (self.board[row][col] ==0)):
                return sum
            else:
                sum+=1
            row -= 1
            col -= 1
        return sum

    def count_down_right(self , row , col , ficha):
        sum = 0
        while ((row<(self.nrows-1)) and (col<(self.ncols-1))):
            if (self.board[row][col] == (-ficha) or (self.board[row][col] ==0)):
                return sum
            else:
                sum+=1
            row += 1
            col += 1
        return sum

    def count_down_left(self , row , col , ficha):
        sum = 0
        while ((row<(self.nrows-1)) and (col>=0)):
            if (self.board[row][col] == (-ficha) or (self.board[row][col] == 0)):
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
        if (self.count_diag_asc(row, col , ficha)==4):
            print("Winner:: " , ficha )
            return ficha
        if (self.count_diag_desc(row , col , ficha)==4):
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
                    self.insert(user , col)
                    win = self.winner(6-int(self.height[col]) , col , user)
                    #self.plot_configuration()
                    #test.print_board()
                    turn += 1
                else:
                    print("Incorrect Col")

            else:
                print("Opponent turn insert a col $$$$----> ")
                col = int(input())-1
                if self.available_site(col):
                    self.insert(opp , col)
                    win = self.winner(6-int(self.height[col]) , col , opp)
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
        self.red_ficha = tk.PhotoImage(file = "images/roja.png")
        #self.blue_ficha = tk.PhotoImage(file = "images/azul.jpg")
        for i in range(self.nrows):
            buttonRow = []
            for j in range(self.ncols):
                button = tk.Button(self.master,text="placeholder",width=100,height=100).grid(row=i,column=j)
                button.bind("<Button-1>",lambda: self.place_piece(ficha,col))
                buttonRow.append(button)
            self.buttons.append(buttonRow)
    def rename_title(self):
        self.master.title("Connect 4")
    
    def change_pic(labelname):
        photo1 = ImageTk.PhotoImage(Image.open("images/roja.png"))
        labelname.configure(image=photo1)
        labelname.photo = photo1

    def place_piece(self,event,ficha,col):
        if self.board.available_site(col):
            self.board.insert(ficha,col)
            height = 6-int(self.board.height[col])
            self.buttons[height][col].config(image=self.red_ficha,compound=tk.RIGHT)
        else:
            tk.messagebox.showinfo("Alert Message" , "This Column is already full")


    def define_labels(self):
        return 0


if __name__ == "__main__":
    #test.evolve_game()

    windows = tk.Tk()
    windows.geometry("1200x1000")
    mainWIndow = gui(windows , 6 , 7,Board(6 , 7))
    windows.mainloop()
