# 숫자의 합
# https://www.acmicpc.net/problem/11720
import sys

def solution():
    n = int(sys.stdin.readline().strip())
    line = sys.stdin.readline().strip()
    sum = 0
    for i in range(n):
        sum += int(line[i])
    print(sum)

solution()