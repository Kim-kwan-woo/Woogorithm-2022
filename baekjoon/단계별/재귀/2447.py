import sys

def solution(N, count, star):
    nextStar = star*4 + ' '*len(star) + star*4
    if count < int(N**(1/3)):
        return solution(N, count+1, nextStar)
    else:
        return nextStar
    
    


if __name__ == "__main__":
    N = int(sys.stdin.readline().rstrip())
    star = solution(N, 1, '*')
    start = 3**(int(N**(1/3))-1)
