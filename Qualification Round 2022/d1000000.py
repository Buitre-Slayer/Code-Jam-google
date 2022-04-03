
def printSolution(t, diceNumFaces):
    diceNumFaces.sort()
    straight = 0
    currentStairValue = 1
    i = 0
    while i < len(diceNumFaces):
        if  currentStairValue <= diceNumFaces[i]:
            straight += 1
            currentStairValue += 1
        i += 1
    print('Case #' + str(t) + ': ' + str(straight))


def readInput():
    T = int(input())
    for t in range(T):
        N = int(input())
        diceNumFaces = [int(x) for x in input().split()]
        printSolution(t + 1, diceNumFaces)
        

if __name__ == '__main__':
    readInput()