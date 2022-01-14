import sys

def solution(string):
    return ord(string)

if __name__ == "__main__":
    string = sys.stdin.readline().rstrip()
    print(solution(string))