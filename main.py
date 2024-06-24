import random

class BattleshipGame:
    def __init__(self):
        self.board_size = 5  # 5x5 grid for simplicity
        self.num_ships = 3   # 3 ships to sink
        self.board = [[' ' for _ in range(self.board_size)] for _ in range(self.board_size)]
        self.ships = []
        self.generate_ships()

    def generate_ships(self):
        for _ in range(self.num_ships):
            ship_row = random.randint(0, self.board_size - 1)
            ship_col = random.randint(0, self.board_size - 1)
            while (ship_row, ship_col) in self.ships:  # Ensure ships don't overlap
                ship_row = random.randint(0, self.board_size - 1)
                ship_col = random.randint(0, self.board_size - 1)
            self.ships.append((ship_row, ship_col))
    
    def print_board(self, hide_ships=False):
        print("  1 2 3 4 5")
        print(" -------")
        for row in range(self.board_size):
            print(f"{row+1}|{'|'.join(self.board[row])}|")
            print(" -------")

    def check_guess(self, guess_row, guess_col):
        if (guess_row < 0 or guess_row >= self.board_size) or (guess_col < 0 or guess_col >= self.board_size):
            print("Oops, that's not even in the ocean.")
            return False
        elif self.board[guess_row][guess_col] == 'X':
            print("You guessed that one already.")
            return False
        else:
            return True

    def play_game(self):
        print("Welcome to Battleship!")
        self.print_board()

        for turn in range(10):  # 10 turns to guess
            print(f"Turn {turn + 1}")
            guess_row = int(input("Guess Row (1-5): ")) - 1
            guess_col = int(input("Guess Col (1-5): ")) - 1

            if not self.check_guess(guess_row, guess_col):
                continue

            if (guess_row, guess_col) in self.ships:
                print("Congratulations! You sunk my battleship!")
                self.board[guess_row][guess_col] = '!'
                self.print_board()
                break
            else:
                print("You missed my battleship!")
                self.board[guess_row][guess_col] = 'X'
                self.print_board()
        
        print("Game Over")

if __name__ == "__main__":
    game = BattleshipGame()
    game.play_game()
