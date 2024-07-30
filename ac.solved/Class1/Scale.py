# 음계
# https://www.acmicpc.net/problem/2920
import sys

def solution():
    scale = list(map(int, sys.stdin.readline().strip().split()))
    diff = scale[0] - scale[1]
    for i in range(1, len(scale)-1):
        if scale[i] - scale[i+1] != diff:
            print('mixed')
            sys.exit()
    if diff == -1:
        print('ascending')
    elif diff == 1:
        print('descending')

solution()