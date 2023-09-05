import random 

"""Creating the game board"""
class GameGrid:

     letters_to_nums = {"A":0, "B":1, "C":2, "D":3, "E":4, "F":5, "G":6, "H":7, "I":8, "J":9}

    def __init__(self, grid):
        self.grid = grid
    
    
    """Printing the rows and columns""" 
    def print_grid(self):
        print(" A B C D E F G H I J") 
        print(" ~~~~~~~~~~~~~~~~~~~")
        row_number = 1
        for row in self.grid:
            print(row_number, "|".join(row))
            row_number += 1

"""Creating the ships"""
class Ships:
    def __init__(self, grid):
        self.grid = GameGrid([[" "] * 10 for i in range(10)])
       
       
    def create_ships(self):
        for i in range(5):
            while True:
                x_row, y_column = random.randint(0, 9), random.randint(0, 9)
                if self.grid.grid[x_row][y_column] != "X":
                    self.grid.grid[x_row][y_column] = "X"
                    break
        return self.grid.grid
    
    """Allowing the user to interact with the game through inputs"""
    def get_user_input(self):
        while True:
            x_row = input("Please enter a row number:\n ")
            if x_row.isdigit():
                x_row = int(x_row)
                if 1 <= x_row <= 10:
                    break
                print("Invalid input, try a number between 1 and 10")
            else:
                print("Now pick a column between A and J")
             
        while True:
            y_column = input("Please enter a column letter:\n ").upper()
            if y_column in "ABCDEFGHIJ" and len(y_column) == 1:
                break
            print("Invalid input, try a letter between A and J")

        return x_row - 1, GameGrid.letters_to_nums.get(y_column)
    
    """Adding a for loop to calculate how many ships are destroyed"""
    def count_sunk_ships(self):
        sunk_ships = 0 
        for row in self.grid.grid:
            for column in row:
                if column == "X":
                    sunk_ships += 1
        return sunk_ships
    
    """Adding the method to run the game"""       
    def run_game(self):
        computer_grid = GameGrid([[" "] * 10 for i in range 10])  
            
        
        """Establishing the number of turns"""
        turns = 10
        while turns > 0:
            self.grid.print_grid()

            user_x_row, user_y_column = self.get_user_input()
            
            """A while loop to give feedback to the user during the game"""
            while self.grid.grid[user_x_row][user_y_column] == "-" or self.grid.grid[user_x_row][user_y_column] == "X":
                print("You already guessed this one, try again")
                user_x_row, user_y_column = self.get_user_input()

            if computer_grid.grid[user_x_row] [user_y_column] == "X":
                print("You sunk my battleship!")
                user_grid.grid[user_x_row] [user_y_column] = "X"

            else:
                print("You missed my battleship!")
                user_grid.grid[user_x_row] [user_y_column] = "-"

            """Checking for win or loose""" 
            if Ships.count_sunk_ships(user_grid) == 5:
                print("You sank all 5 battleships!")
                break

            elif turns == 0: 
                print("Sorry, you have no more turns left!")
                GameGrid(self.grid.grid).print_grid()

            turns -= 1

if __name__ == "__main__":
    game = Ships()
    game.create_ships()
    game.run_game()



    


