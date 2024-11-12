import numbers
import pyfiglet
import termcolor
import sys
import os

class Board:
    def __init__(self, N):
        # Initialize board size and properties
        self.size = N
        self.arr = []  # board's structure, a 2D array for cell values
        self.str = ""  # board's visual appearance as a string

    def structure(self):
        # Sets up the board with numbered cells (1 to N*N) to represent empty spaces
        self.arr = [[0 for j in range(self.size)] for i in range(self.size)]
        p = 1  # Start numbering from 1
        for i in range(self.size):
            for j in range(self.size):
                self.arr[i][j] = p
                p += 1
    
    def appearance(self):
        # Generates the visual appearance of the board with '|' and '-' separators
        self.str = ""
        for i in range(self.size):
            for j in range(self.size):
                if j != self.size - 1:
                    self.str += str(self.arr[i][j]) + " | "
                else:
                    self.str += str(self.arr[i][j]) + "\n"
            if i != self.size - 1:
                self.str += 3 * self.size * "-" + "\n"

    def add(self, index, val):
        # Marks the board cell at `index` with the player's marker (X or O)
        index -= 1
        r = index % self.size
        d = index // self.size
        if isinstance(self.arr[d][r], int):  # Check if the cell is not already taken
            self.arr[d][r] = val
            return True
        else:
            print("Cell already taken. Choose another one.")
            return False

    def is_filled(self):
        # Checks if the board is completely filled
        for i in range(self.size):
            for j in range(self.size):
                if isinstance(self.arr[i][j], numbers.Real):
                    return False  # Returns False if any cell still holds a number
        return True
                
    def check_diagonals(self):
        # Checks if any of the diagonals have the same value across all cells
        b1 = True  # Primary diagonal
        b2 = True  # Secondary diagonal
        N = self.size - 1
        for i in range(N):
            if self.arr[i][i] != self.arr[i + 1][i + 1]:
                b1 = False
        for j in range(N):
            if self.arr[j][N - j] != self.arr[j + 1][N - (j + 1)]:
                b2 = False
        return b1 or b2
    
    def check_rows(self):
        # Checks if any row has the same value across all cells
        b = False
        N = self.size
        for i in range(N):
            b1 = True
            for j in range(N - 1):
                if self.arr[i][j] != self.arr[i][j + 1]:
                    b1 = False
            b = b or b1
        return b

    def check_columns(self):
        # Checks if any column has the same value across all cells
        b = False
        N = self.size
        for j in range(N):
            b1 = True
            for i in range(N - 1):
                if self.arr[i][j] != self.arr[i + 1][j]:
                    b1 = False
            b = b or b1
        return b

    def check_win(self):
        # Checks if there is a win condition on the board
        return self.check_diagonals() or self.check_rows() or self.check_columns()
    
class Player:
    def __init__(self, Name, n):
        # Initialize player with name and score
        self.name = Name
        self.score = n

def clear_screen():
    # Clears the console screen based on the operating system
    os.system("cls" if os.name == "nt" else "clear")

def update_display(text):
    # Updates the display in the console
    sys.stdout.write('\r' + ' ' * len(text))
    sys.stdout.write('\r' + text)
    sys.stdout.flush()

def welcome():
    # Displays welcome text and game title
    print(pyfiglet.figlet_format("Welcome to \n"))
    print(termcolor.colored(pyfiglet.figlet_format("                Tic-Tac-Toe \n"), color="yellow"))
    print("enter your choice (choose between 1 and 4) \n")

def register_players(p1, p2):
    # Registers names for two players
    print("for the first player (who wants the X)")
    Name = input("enter your name : ")
    p1.name = Name
    print("for the second player")
    Name = input("enter your name : ")
    p2.name = Name

def view_score(p1, p2):
    # Displays the current score for both players
    if p1.name == "" or p2.name == "":
        print("please make sure to enter your names first \n")
    else:
        print(p1.name + "'s score : " + str(p1.score) + "\n")
        print(p2.name + "'s score : " + str(p2.score) + "\n")

def game(p1, p2):                     
    # Manages the main game logic, alternating turns between two players
    if p1.name == "" or p2.name == "":
        print("please make sure to enter your names first \n")
    else:
        print(termcolor.colored("enjoy the game ! \n", color="yellow"))
        B = Board(3)  # Initialize a 3x3 Tic-Tac-Toe board
        winner = p2
        B.structure()  # Set up the board structure with initial values
        B.appearance()  # Update the visual appearance
        print("you choose a number from 1 to 9 \n")
        print(B.str)
        while not B.is_filled() and not B.check_win():
            # Player 1's turn
            num = input(termcolor.colored(p1.name + "'s turn \n", color="red"))
            while not num.isnumeric() or int(num) > 9 or int(num) < 1:
                num = input(termcolor.colored(p1.name + "'s turn \n enter a valid number (1-9)", color="red"))
            
            B.add(int(num), "X")
            B.appearance()
            clear_screen()
            update_display(B.str)
            if B.is_filled() or B.check_win():
                winner = p1
                break
            # Player 2's turn
            num = input(termcolor.colored(p2.name + "'s turn \n", color="blue"))
            while not num.isnumeric() or int(num) > 9 or int(num) < 1:
                num = input(termcolor.colored(p1.name + "'s turn \n enter a valid number (1-9)", color="blue"))
            
            B.add(int(num), "O")
            B.appearance()
            clear_screen()
            update_display(B.str)
        
        # Game result based on board state
        if B.is_filled() and not B.check_win():
            print("DRAW")
        if B.check_win():
            print(termcolor.colored("CONGRATS TO " + winner.name, color="yellow"))
            winner.score += 1

def Tic_Tac_Toe():
    # Main function to start and control the game flow
    p1 = Player("", 0)
    p2 = Player("", 0)
    welcome()
    choice = input("1) enter your names \n2) view your score \n3) play \n4) exit \n")
    while int(choice) != 4:
        if int(choice) == 1:
            clear_screen()
            register_players(p1, p2)
        elif int(choice) == 2:
            clear_screen()
            view_score(p1, p2)
        elif int(choice) == 3:
            clear_screen()
            game(p1, p2)
        else:
            clear_screen()
            print("invalid choice ! (choose between 1 and 4) \n")
        choice = input("1) enter your names \n2) view your score \n3) play \n4) exit \n")
    print(termcolor.colored("Thank you for playing !", color="yellow"))

# Start the game
Tic_Tac_Toe()