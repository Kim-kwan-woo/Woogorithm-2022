import sys

def solution(x, y):
    if x > 0 and y > 0:
        return 1
    elif x < 0 and y > 0:
        return 2
    elif x < 0 and y < 0:
        return 3
    else:
        return 4
    
    

if __name__ == "__main__":
    x = int(sys.stdin.readline().rstrip())
    y = int(sys.stdin.readline().rstrip())
    print(solution(x, y))