# 알파벳 찾기
# https://www.acmicpc.net/problem/10809
import sys

def solution():
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    word = sys.stdin.readline().strip()
    result = []
    for i in range(len(alphabet)):
        result.append(word.find(alphabet[i]))
    print(' '.join(str(i) for i in result))

solution()