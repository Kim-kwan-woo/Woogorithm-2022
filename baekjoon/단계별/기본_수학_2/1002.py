import sys

def solution(x1, y1, r1, x2, y2, r2):
    distance = ((x2-x1)**2 + (y2-y1)**2)**(1/2)

    if distance != 0: # 두 점이 같은 위치가 아닌 경우
        if (r1 + r2 == distance) or (abs(r1-r2) == distance):
            return 1
        elif (r1 + r2 < distance) or (abs(r1-r2) > distance):
            return 0
        else:
            return 2
    else: # 두 점이 같은 위치인 경우
        if r1 == r2: #원이 되므로 무한개
            return -1
        else:
            return 0

if __name__ == "__main__":
    T = int(sys.stdin.readline().rstrip())
    answer = []
    for i in range(T):
        x1, y1, r1, x2, y2, r2 = map(int, sys.stdin.readline().split())
        answer.append(solution(x1, y1, r1, x2, y2, r2))

    for i in answer:
        print(i)