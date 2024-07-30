# 구구단
# https://www.acmicpc.net/problem/2739
def solution():
    dan = int(input())
    for i in range(1, 10):
        print(dan, '*', i, '=', dan*i)

solution()