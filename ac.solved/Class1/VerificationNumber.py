# 검증수
# https://solved.ac/class?class=1
def solution():
    sum = 0
    for i in map(int, input().split()):
        sum += i**2
    print(sum%10)

solution()