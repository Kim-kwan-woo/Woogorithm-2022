import sys

def solution():
    length = [1]
    for i in range(1, len(A)):
        if A[i] > A[i-1]:
            length.append(length[i-1]+1)
        else:
            length.append(length[i-1])

    return length[-1]

        


if __name__ == "__main__":
    N = int(sys.stdin.readline().rstrip())
    A = list(map(int, sys.stdin.readline().split()))
    print(solution())

