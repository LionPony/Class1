# X보다 작은 수
# https://www.acmicpc.net/problem/10871
def solution():
    n, x = map(int, input().split())
    sequence = input().split()

    answer = []
    for i in sequence:
        if int(i) < x:
            answer.append(i)
    
    print(' '.join(answer))

solution()