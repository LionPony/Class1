# A+B - 5
# https://www.acmicpc.net/problem/10952
import sys

def solution():
    end = False
    while end == False:
        a, b = map(int, sys.stdin.readline().split())
        if a == 0 and b == 0:
            end = True
        else:
            print(a+b)

solution()