import sys

def solution():
    #2의 개수와 5의 개수를 세서 짝을 맞추면 그 개수만큼 뒤에서 0의 개수가 된다.
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
    