from board import Board

def part2(fileName):
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

    c = []

    for guess in guesses:
        z = 0
        for b in boards:
            if b in c:
                continue
            b.checkGuess(guess)
            if len(boards) != 1:
                if(b.checkWin(guess, True)):
                    c.append(b)
            if len(boards) == len(c):
                winner = b.checkWin(guess, False)
                if winner != None:
                    return winner
            z += 1

print(part2("Input.txt"))
