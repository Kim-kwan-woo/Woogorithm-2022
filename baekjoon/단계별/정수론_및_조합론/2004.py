import sys

def solution():
    #2의 개수와 5의 개수를 세서 짝을 맞추면 그 개수만큼 뒤에서 0의 개수가 된다.
    two = twoCount(n) - twoCount(m) - twoCount(n-m)
    five = fiveCount(n) - fiveCount(m) - fiveCount(n-m)

    return min(two, five)

def twoCount(n):
    count = 0
    while n != 0:
        n //= 2
        count += n
    return count

def fiveCount(n):
    count = 0
    while n != 0:
        n //= 5
        count += n
    return count




if __name__ == "__main__":
    n, m = map(int, sys.stdin.readline().split())
    
    print(solution())
    