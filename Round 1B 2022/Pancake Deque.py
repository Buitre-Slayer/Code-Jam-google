def solve(t, deque):
    maxValueFound = -100
    count = 0
    while deque:
        if deque[0] <= deque[-1]:
            if maxValueFound <= deque[0]:
                maxValueFound = deque[0]
                count += 1
            deque.pop(0)
        else:
            if maxValueFound <= deque[-1]:
                maxValueFound = deque[-1]
                count += 1
            deque.pop()
    print('Case #' + str(t) + ': ' + str(count))


def readInput():
    T = int(input())
    for t in range(T):
        N = input()
        deque = [int(x) for x in input().split()]
        solve(t + 1, deque)

if __name__ == '__main__':
    readInput()