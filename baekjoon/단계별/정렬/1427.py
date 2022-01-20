import sys

def solution(N):
    return ''.join(sorted(N, reverse=True))


        

if __name__ == "__main__":
    N = sys.stdin.readline().rstrip()

    print(solution(N))