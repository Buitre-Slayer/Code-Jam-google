
def deepSearch(t, products, N):
    bestSolution = 10000000000000000000000
    # Level, sum, position
    stack = [[1, max(products[0]), max(products[0])]]
    while stack:
        currentPosibility = stack[0]
        if currentPosibility[0] >= N:
            bestSolution = min(bestSolution, currentPosibility[1])
        else:
            leftBoundary = min(products[currentPosibility[0]])
            rightBoundary = max(products[currentPosibility[0]])
            if leftBoundary >= currentPosibility[2]:
                stack.append([currentPosibility[0] + 1, currentPosibility[1] + (rightBoundary - currentPosibility[2]), rightBoundary])
            elif rightBoundary <= currentPosibility[2]:
                stack.append([currentPosibility[0] + 1, currentPosibility[1] + (currentPosibility[2] - leftBoundary), leftBoundary])
            else:
                stack.append([currentPosibility[0] + 1, 
                currentPosibility[1] + (currentPosibility[2] - leftBoundary) + (rightBoundary - leftBoundary), rightBoundary])

                stack.append([currentPosibility[0] + 1, 
                currentPosibility[1] + (rightBoundary - currentPosibility[2]) + (rightBoundary - leftBoundary), leftBoundary])
        stack.pop(0)
    print('Case #' + str(t) + ': ' + str(bestSolution))


def readInput():
    T = int(input())
    for t in range(T):
        N, P = [int(x) for x in input().split()]
        products = []
        for n in range(N):
            products.append([int(x) for x in input().split()])
        deepSearch(t + 1, products, N)

if __name__ == '__main__':
    readInput()