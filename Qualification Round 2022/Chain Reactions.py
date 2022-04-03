from queue import PriorityQueue

visited = [0] * 100002

def generateReverseConection(conection):
    c = [[] for x in range(100005)]
    i = 0
    while i < len(conection):
        if conection[i] != -1:
            c[conection[i]].append(i)
        i += 1
    return c





def solve(fun, conection, inverseConection, t):
    global visited
    i = 0
    sum = 0
    while i < len(conection):
        if conection[i] == -1:
            visited[i] = 1
            pq = PriorityQueue()
            pq.put((fun[i], i))
            maxValue = 0
            nextPos = [i]
            while True:
                pos = pq.get()[1]
                visited[pos] = True
                if fun[pos] >= maxValue:
                    maxValue = fun[pos]
                    
                anyParent = False
                for c in inverseConection[pos]:
                    pq.put((fun[c], c))
                    anyParent = True
                        
                if not anyParent:
                    sum += maxValue
                    nextPos.pop(0)
                    while not pq.empty():
                        nextPos.append(pq.get()[1])
                    if not nextPos:
                        break
                    else:
                        pq.put((fun[nextPos[0]],nextPos[0]))
                        maxValue = 0
        i += 1
    print('Case #' + str(t) + ': ' + str(sum))


def readInput():
    T = int(input())
    for t in range(T):
        N = int(input())
        fun = [int(x) for x in input().split()]
        conection = [int(x) - 1 for x in input().split()]
        inverseConection = generateReverseConection(conection)
        solve(fun, conection, inverseConection, t + 1)


if __name__ == '__main__':
    readInput()