class Board:

    def __init__(self):
        self.board = []

    def addRow(self, row):
        rowList = row.split()
        self.board.append(rowList)

    # For debugging - Prints in readable format
    def printGame(self):
        for x in self.board:
            print(f"{x}\n")
        print("Next\n")

    def checkGuess(self, guess):
        i = 0
        for row in self.board:
            if guess in row:
                index = row.index(guess)
                self.board[i][index] = "X"
                break
            i += 1

    def checkWin(self, guess, part2):
        winner = False
        for row in self.board:
            if row.count("X") == len(row):
                winner = True
        rotated = zip(*self.board[::-1]) #Straight from stack overflow
        for row in rotated:
            if row.count("X") == len(row):
                winner = True
        if not part2:
            if winner:
                total = 0
                for row in self.board:
                    for num in row:
                        if num != "X":
                            total += int(num)

                return total * int(guess)
        if part2:
            if winner:
                return True
        return None



    

