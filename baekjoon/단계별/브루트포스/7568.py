import sys

def solution(N, people):
    answer = []
    for i in range(N):
        count = 0
        for j in range(N):
            if i == j:
                continue
            if people[i][0] < people[j][0] and people[i][1] < people[j][1]:
                count += 1

        answer.append(count+1)
    return answer


if __name__ == "__main__":
    N = int(sys.stdin.readline().rstrip())
    people = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

    for i in solution(N, people):
        print(i, end=' ')