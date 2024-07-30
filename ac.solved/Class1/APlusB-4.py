# A+B - 4
# https://www.acmicpc.net/problem/10951
import sys

def solution():
    while True:
        try:
            a, b = map(int, sys.stdin.readline().split())
            print(a+b)
        except:
            break

solution()