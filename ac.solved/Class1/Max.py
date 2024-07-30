# 최댓값
# https://www.acmicpc.net/problem/2562
import sys

def solution():
    list = []
    for i in range(9):
        list.append(int(sys.stdin.readline().strip()))
    print(max(list))
    print(list.index(max(list))+1)

solution()