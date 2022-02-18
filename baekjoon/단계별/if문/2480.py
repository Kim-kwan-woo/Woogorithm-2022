import sys

def solution():
    if a == b and a == c:
        return 10000+a*1000
    elif a != b and a != c and b != c:
        return max(a, b, c)*100
    else:
        if a == b or a == c:
            return 1000+a*100
        else:
            return 1000+b*100


if __name__ == "__main__":
    a, b, c = map(int, sys.stdin.readline().split())
    
    print(solution())
    