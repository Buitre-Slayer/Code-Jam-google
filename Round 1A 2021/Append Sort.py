def getIntAsList(value):
    r = []
    for i in str(value):
        r.append(int(i))
    return r


def allNine(a, b):
    for i, j in zip(a, b):
        if i - j != 9: return False
    return True


def matchLength(a, b):
    while len(getIntAsList(a)) < len(getIntAsList(b)):
        a *= 10
    return a


def solve(t, values):
    i = 1
    operations = 0
    while i < len(values):
        if not values[i - 1] < values[i]:
            greater, lower = False, False
            for a, b in zip(getIntAsList(values[i - 1]), getIntAsList(values[i])):
                if b > a:
                    greater = True
                    break
                elif b < a:
                    lower = True
                    break
            aux = 0
            if greater:
                aux = matchLength(values[i], values[i - 1])
            elif lower:
                aux = matchLength(values[i], values[i - 1])
                aux *= 10
            else:
                if values[i - 1] == values[i]:
                    aux = values[i]
                    aux *= 10
                else:
                    aux = matchLength(values[i], values[i - 1])
                    if allNine(getIntAsList(values[i - 1])[len(getIntAsList(values[i])):], 
                            getIntAsList(aux)[len(getIntAsList(values[i])):]):
                        aux *= 10
                    else:
                        aux = values[i - 1] + 1
            operations += len(getIntAsList(aux)) - len(getIntAsList(values[i]))
            values[i] = aux
        i += 1
    print('Case #' + str(t) + ': ' + str(operations))


def readInput():
    T = int(input())
    for t in range(T):
        N = int(input())
        values = [int(x) for x in input().split()]
        solve(t + 1, values)

if __name__ == '__main__':
    readInput()