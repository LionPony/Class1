# 별찍기 - 1
# https://www.acmicpc.net/problem/2438
def solution():
    count = int(input())
    i = 1
    while i <= count:
        for j in range(i):
            print('*', end='')
        print('')
        i += 1

solution()