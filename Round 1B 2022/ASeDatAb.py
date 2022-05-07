
def solve():
    print('10000000')
    n = int(input())
    i = 1
    while n != 0 and i < 300:
        if n == 8:
            print('11111111')
        elif n == 7:
            print('01111111')
        elif n == 1:
            print('10000000')
        elif n == 6:
            print('01010111')
        elif n == 3:
            print('10101000')
        else:
            print('01010101')
        n = int(input())
        i += 1
        


def readInput():
    T = int(input())
    for t in range(T):
        solve()

if __name__ == '__main__':
    readInput()