# 숫자의 개수
# https://www.acmicpc.net/problem/2577
import sys

def solution():
    a = int(sys.stdin.readline().strip())
    b = int(sys.stdin.readline().strip())
    c = int(sys.stdin.readline().strip())

    result = str(a*b*c)
    answer = [0 for i in range(10)]
    for i in range(len(result)):
        answer[int(result[i])] += 1

    for i in range(len(answer)):
        print(answer[i])
solution()