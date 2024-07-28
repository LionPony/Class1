# 최소, 최대
# https://www.acmicpc.net/problem/10818
import sys

def solution():
    n = int(sys.stdin.readline().strip())
    line = list(map(int, sys.stdin.readline().strip().split()))
    print(min(line), max(line))

solution()