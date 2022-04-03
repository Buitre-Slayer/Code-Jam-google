def readPrinterInkValues():
    return [int(x) for x in input().split()]


def maxSelectable(printer, i):
    return min([x[i] for x in printer])


def printSolution(t, printer):
    remaining = 1000000
    selections = []
    for i in range (4):
        selections.append(min(remaining, maxSelectable(printer, i)))
        remaining -= selections[i]
    if remaining == 0:
        solution = ' '.join([str(x) for x in selections])
    else:
        solution = 'IMPOSSIBLE'
    print('Case #' + str(t + 1) + ': ' + solution)


def readInput():
    T = int(input())
    for t in range(T):
        printer = [readPrinterInkValues(), readPrinterInkValues(), readPrinterInkValues()]
        printSolution(t, printer)

if __name__ == '__main__':
    readInput()