from board import Board

def part1(fileName):
    with open(fileName) as input:
        input = input.read()
        list = input.split("\n")
    
    guesses = list[0].split(",")
    del list[0]
    boards = [Board() for _ in range(list.count(""))]
    i = 1
    p = 0
    while i < len(list):
        b = boards[p]
        b.addRow(list[i])
        b.addRow(list[i+1])
        b.addRow(list[i+2])
        b.addRow(list[i+3])
        b.addRow(list[i+4])
        i += 6
        p += 1

    for guess in guesses:
        for b in boards:
            b.checkGuess(guess)
            winner = b.checkWin(guess, False)
            if winner != None:
                return winner

print(part1("Input.txt"))