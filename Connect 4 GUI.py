from tkinter import *
import tkinter.messagebox

class Connect4Game:
    def __init__(self):
        self.root = Tk()
        self.root.title("Connect 4")
        self.root.geometry("400x400")
        self.root.resizable(0,0)
        self.player_1 = True
        self.canvas = Canvas(self.root, width=400, height=400, bg="white")
        self.canvas.grid(row=0, column=0)
        self.canvas.bind("<Button-1>", self.makeMove)
        self.board = [[0 for x in range(7)] for y in range(6)]
        self.game_over = False
        self.drawBoard()
        self.root.mainloop()

    #draws a board
    def drawBoard(self):
        for row in range(7):
            for col in range(6):
                x1 = row*50
                y1 = col*50
                x2 = (row+1)*50
                y2 = (col+1)*50
                self.canvas.create_rectangle(x1, y1, x2, y2, fill="white")
                
    # places a piece on the game board when a player clicks on the canvas.
    # red or yellow, depending on the current player.
    def makeMove(self, event):
        if self.game_over:
            return
        x, y = event.x, event.y
        col = int(x/50)
        if col < 0 or col > 6:
            return
        row = self.getRowIndex(col)
        if row < 0 or row > 5:
            return
        color = "red" if self.player_1 else "yellow"
        self.canvas.create_oval(col*50+2, row*50+2, (col+1)*50-2, (row+1)*50-2, fill=color)
        self.board[row][col] = 1 if self.player_1 else 2
        self.player_1 = not self.player_1
        self.isWinner(row, col)

    #returns the index of lowest available space. If all of the rows in the column are full, it returns -1.
    def getRowIndex(self, col):
        for row in range(5, -1, -1):
            if self.board[row][col] == 0:
                return row
        tkinter.messagebox.showinfo("Connect 4",  "Invalid Move, Column Full!")
        return -1

    #checks if a player has won the game.
    def isWinner(self, row, col):

        # checks the colour counter being placed 
        colour = "yellow" if self.player_1 else "red"
        print ("Last Move:", colour)


        #check horizontal
        count = 1
        for i in range(col+1, 7):
            if self.board[row][i] == self.board[row][col]:
                count += 1
            else:
                break
        for i in range(col-1, -1, -1):
            if self.board[row][i] == self.board[row][col]:
                count += 1
            else:
                break
        if count >= 4:
            self.game_over = True

            # displays pop up message with the winner
            if colour == "red":
                tkinter.messagebox.showinfo("Connect 4",  "Red Player Wins!")
            if colour == "yellow":
                tkinter.messagebox.showinfo("Connect 4",  "Yellow Player Wins!")
            return
        
        #check vertical
        count = 1
        for i in range(row+1, 6):
            if self.board[i][col] == self.board[row][col]:
                count += 1
            else:
                break
        for i in range(row-1, -1, -1):
            if self.board[i][col] == self.board[row][col]:
                count += 1
            else:
                break
        if count >= 4:
            self.game_over = True
            if colour == "red":
                tkinter.messagebox.showinfo("Connect 4",  "Red Player Wins!")
            if colour == "yellow":
                tkinter.messagebox.showinfo("Connect 4",  "Yellow Player Wins!")
            return
        
        #check diagonal negative
        count = 1
        x, y = row, col
        while x < 5 and y < 6:
            x += 1
            y += 1
            if self.board[x][y] == self.board[row][col]:
                count += 1
            else:
                break
        x, y = row, col
        while x > 0 and y > 0:
            x -= 1
            y -= 1
            if self.board[x][y] == self.board[row][col]:
                count += 1
            else:
                break
        if count >= 4:
            self.game_over = True
            if colour == "red":
                tkinter.messagebox.showinfo("Connect 4",  "Red Player Wins!")
            if colour == "yellow":
                tkinter.messagebox.showinfo("Connect 4",  "Yellow Player Wins!")
            return
        
        #check diagonal positive 
        count = 1
        x, y = row, col
        while x > 0 and y < 6:
            x -= 1
            y += 1
            if self.board[x][y] == self.board[row][col]:
                count += 1
            else:
                break
        x, y = row, col
        while x < 5 and y > 0:
            x += 1
            y -= 1
            if self.board[x][y] == self.board[row][col]:
                count += 1
            else:
                break
        if count >= 4:
            self.game_over = True
            #shows text box displaying who won
            if colour == "red":
                tkinter.messagebox.showinfo("Connect 4",  "Red Player Wins!")
            if colour == "yellow":
                tkinter.messagebox.showinfo("Connect 4",  "Yellow Player Wins!")
            return

game = Connect4Game()
