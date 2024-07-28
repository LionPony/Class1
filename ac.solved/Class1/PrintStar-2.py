# 별 찍기 - 2
# https://www.acmicpc.net/problem/2439
import sys

def solution():
    n = int(sys.stdin.readline().strip())
    for i in range(1, n+1):
        for j in range(n-i):
            print(' ', end='')
        for j in range(n-i, n):
            print('*', end='')
        print('')

solution()