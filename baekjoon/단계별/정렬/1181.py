import sys

def solution(strings):
    return sorted(set(strings), key= lambda x: (len(x), x))


        

if __name__ == "__main__":
    N = int(sys.stdin.readline().rstrip())
    strings = [sys.stdin.readline().rstrip() for _ in range(N)]

    for i in solution(strings):
        print(i)