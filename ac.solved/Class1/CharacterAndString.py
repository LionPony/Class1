# 문자와 문자열
# https://www.acmicpc.net/problem/27866
import sys

def solution():
    string = sys.stdin.readline().strip()
    index = int(sys.stdin.readline().strip())
    print(string[index-1])

solution()