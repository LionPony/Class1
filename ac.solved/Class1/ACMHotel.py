# ACM 호텔
# https://www.acmicpc.net/problem/10250
import sys

def solution():
    t = int(sys.stdin.readline().strip())
    for i in range(t):
        h, w, n = map(int, sys.stdin.readline().strip().split())
        if n%h == 0:
            x = n//h
            y = h
        else:
            x = (n//h)+1
            y = n%h

        print(f"{y}{x:02}")

solution()