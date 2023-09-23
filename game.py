# Python TicTacToe game with Tk GUI and minimax AI
# Author: NIKHIL <nikhiljangra264@gmail.com>

from tkinter import Tk, Button, Label, StringVar, Radiobutton, Frame, OptionMenu
from tkinter.font import Font
from board import Board
from header import SIZE, MARK
from engine import engine

class GUI:
    def __init__(self) -> None:
        self.app = Tk()
        self.app.title('Tic-Tac-Toe')
        self.app.geometry("500x500")

        # Create a frame to center the elements
        self.center_frame = Frame(self.app, bg="#f2f2f2")
        self.center_frame.pack(expand=True)

        self.board = None
        self.diff = 0
        self.engine = None
        self.turn = MARK.PLAYER_1
        self.font = Font(family='Helvetica', size=32, weight="bold")
        self.buttons = []

        self.gamemode = StringVar() # variable to store game mode
        self.gamemode.set("PvP")  # Set a default game mode

        self.difficulty = StringVar()  # variable to store difficulty level
        self.difficulty.set("Medium")  # Set a default difficulty level

        mode_label = Label(self.center_frame, 
                           text='Select game mode: ',
                           bg='#f2f2f2', font=('Helvetica',14))
        mode_label.grid(row=0, column=0, columnspan=SIZE,sticky='WE', padx=10)

        # radio button for selecting mode
        player_vs_player = Radiobutton(self.center_frame,
                                       text="Player vs Player",
                                       variable=self.gamemode, 
                                       value="PvP", 
                                       font=('Helvetica', 12))
        player_vs_player.grid(row=1, column=0, columnspan=SIZE, sticky="WE")

        player_vs_computer = Radiobutton(self.center_frame, 
                                         text="Player vs Computer", 
                                         variable=self.gamemode, 
                                         value="PvC", 
                                         font=('Helvetica', 12))
        player_vs_computer.grid(row=2, column=0, columnspan=SIZE, sticky="WE")

        # OptionMenu for selecting difficulty level
        difficulty_label = Label(self.center_frame, 
                                 text='Select difficulty: ',  
                                 bg='#f2f2f2', font=('Helvetica', 14))
        difficulty_label.grid(row=3, column=0, columnspan=SIZE, sticky='WE', padx=10)

        difficulty_options = ["Easy", "Medium", "Hard"]
        difficulty_menu = OptionMenu(self.center_frame, 
                                     self.difficulty, 
                                     *difficulty_options,)
        difficulty_menu.config(font=('Helvetica', 12))
        difficulty_menu.grid(row=4, column=0, columnspan=SIZE, sticky="WE")

        start_button = Button(self.center_frame, 
                              text='Start Game', 
                              command=self.start_game, 
                              font=('Helvetica', 14), 
                              bg='#4CAF50', 
                              fg='white', 
                              activebackground='#45a049')
        start_button.grid(row=5, column=0, columnspan=SIZE, sticky="WE")

        # Create an info label
        self.info_label = Label(self.center_frame, 
                                text='', 
                                font=('Helvetica', 16, 'bold'), 
                                bg='#f2f2f2')
        self.info_label.grid(row=6, column=0, columnspan=SIZE, sticky="WE")

    def start_game(self):
        self.board = Board()
        if self.gamemode.get() == 'PvC':
            difficulty = self.difficulty.get()
            if difficulty == "Easy":
                self.diff = 2
            elif difficulty == "Medium":
                self.diff = 5
            elif difficulty == "Hard":
                self.diff = 8
            self.engine = engine(MARK.PLAYER_1, MARK.PLAYER_2, self.diff)

        # Remove game mode selection widgets
        for widget in self.center_frame.winfo_children():
            if widget != self.info_label:  # Skip destroying the info_label
                widget.destroy()
        self.info_label.config(text="    X move    ")

        for x in range(SIZE):
            for y in range(SIZE):
                button = Button(self.center_frame, 
                                command=lambda x=x, y=y: self.move(x,y), 
                                text='', 
                                state='normal', 
                                font=self.font, 
                                width=3, 
                                height=1, 
                                bg='#FFFFFF', 
                                activebackground='#E1E1E1',
                                disabledforeground='#000000')
                button.grid(row=x, column=y, padx=5, pady=5)
                self.buttons.append(button)
        reset_button = Button(self.center_frame, text='Reset', command=self.reset, 
                              font=('Helvetica', 14), 
                              bg='#f44336',
                              fg='white', 
                              activebackground='#d32f2f')
        reset_button.grid(row = SIZE, column=0, columnspan=SIZE, sticky="WE", pady=10)

    def move(self, x, y):
        if self.board is None:
            return
        
        pos = (x * SIZE) + y
        if self.board[pos] == MARK.EMPTY:
            self.board[pos] = self.turn
            self.buttons[pos]['text'] = 'X' if self.turn == MARK.PLAYER_1 else 'O'
            self.buttons[pos]['state'] = 'disabled'

            self.turn = MARK.PLAYER_2 if self.turn == MARK.PLAYER_1 else MARK.PLAYER_1

            winner = self.board.check()
            if winner != MARK.EMPTY:
                if winner == MARK.PLAYER_1:
                    info_text = "    X wins    "
                else:
                    info_text = "    O wins    "
                self.info_label.config(text=info_text)
                self.disable_all_button()
                return
            elif not self.board.has_empty():
                info_text = " It's a tie!  "
                self.info_label.config(text=info_text)
                self.disable_all_button()
                return
            else:
                if self.turn == MARK.PLAYER_1:
                    info_text = "    X move    "
                else:
                    info_text = "    O move    "

            self.info_label.config(text=info_text)

            if self.gamemode.get() == 'PvC' and self.turn == MARK.PLAYER_2:
                computer_move = self.engine.run(self.board, self.turn)
                self.move(computer_move // SIZE, computer_move % SIZE)  # Make the computer's move
    
    def disable_all_button(self):
        for button in self.buttons:
            button['state'] = 'disabled'

    def reset(self):
        if self.board is None:
            return
        
        self.board.reset()
        self.turn = MARK.PLAYER_1
        for button in self.buttons:
            button['text'] = ''
            button['state'] = 'normal'
        self.info_label.config(text="    X move    ")

    def mainloop(self):
        self.app.mainloop()


if __name__=='__main__':
    GUI().mainloop()

