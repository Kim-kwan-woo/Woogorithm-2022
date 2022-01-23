import sys

def solution(N, start, end):
    if N == 1:
        print(start, end)
        return
    
    solution(N-1, start, 6-start-end)
    print(start, end)
    solution(N-1, 6-start-end, end)


if __name__ == "__main__":
    N = int(sys.stdin.readline().rstrip())
    print(2**N-1)
    solution(N, 1, 3)
    


