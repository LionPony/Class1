# 나머지
# https://www.acmicpc.net/problem/3052
import sys

def solution():
    answer = set()
    for i in range(10):
        answer.add(int(sys.stdin.readline().strip())%42)
    print(len(answer))

solution()