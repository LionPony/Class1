# 두 수 비교하기
# https://www.acmicpc.net/problem/1330
def solution():
    a, b = map(int, input().split())
    if a > b:
        print('>')
    elif a < b:
        print('<')
    else:
        print('==')

solution()