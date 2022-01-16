import sys

def solution(a, b, c):
    maxLen = max(a, b, c)
    tempNum = 0
    if a != maxLen:
        tempNum += a**2
    if b != maxLen:
        tempNum += b**2
    if c != maxLen:
        tempNum += c**2

    return "right" if tempNum == maxLen**2 else "wrong"


if __name__ == "__main__":
    answer = []
    while True:
        a, b, c = map(int,sys.stdin.readline().split())
        if a == 0 and b == 0 and c == 0:
            break

        answer.append(solution(a, b, c))

    for i in answer:
        print(i)