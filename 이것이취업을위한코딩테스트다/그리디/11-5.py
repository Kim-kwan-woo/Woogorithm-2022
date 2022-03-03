import sys

N, M = map(int, sys.stdin.readline().split())
balls = list(map(int, sys.stdin.readline().split()))

count = 0
for i in range(N-1):
    for j in range(i+1, N):
        if i != j:
            count += 1

print(count)
