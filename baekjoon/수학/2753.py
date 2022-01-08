import sys

def solution(year):
    if year % 4 == 0 and year % 100 != 0:
        return 1
    elif year % 400 == 0:
        return 1
    else:
        return 0
    
    

if __name__ == "__main__":
    year = int(sys.stdin.readline().rstrip())
    print(solution(year))