import sys

def solution():
    multi = [1]*(n+1)

    for i in range(1, n+1):
        multi[i] = multi[i-1]*i

    binomialCoefficient = str(multi[n]//(multi[m]*multi[n-m]))
    count = 0

    for i in range(len(binomialCoefficient)-1, -1, -1):
        if binomialCoefficient[i] == "0":
            count += 1
        else:
            break

    return count



if __name__ == "__main__":
    n, m = map(int, sys.stdin.readline().split())
    
    print(solution())
    