def printSequence(i, C):
    if i == 0:
        print('+-' * C + '+')
    else:
        print('|.' * C + '|')

def printAnswere(T, R, C):
    print("Case #" + str(T) + ':')
    print(".." + "+-" * (C - 1) + '+')
    print('..' + '|.' * (C - 1) + '|')
    printSequence(0, C)
    for i in range(R):
        printSequence(1, C)
        printSequence(0, C)

def main():
    T = int(input())
    for t in range(T):
        R, C = [int(x) for x in input().split()]
        R -= 1
        printAnswere(t + 1, R, C)
        

main()