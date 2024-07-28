# A + B - C
# https://www.acmicpc.net/problem/31403
import sys

def solution():
    a = sys.stdin.readline().strip()
    b = sys.stdin.readline().strip()
    c = sys.stdin.readline().strip()

    print(int(a)+int(b)-int(c))
    print(int(a+b)-int(c))

solution()