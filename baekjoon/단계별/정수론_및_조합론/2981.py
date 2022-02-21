import sys
import math

def solution(numbers):
    
    numbers = sorted(numbers)
    interval = []
    answer = []
    for i in range(1, N):
        interval.append(numbers[i] - numbers[i-1])

    tempGCD = interval[0]
    for i in range(1, len(interval)):
        tempGCD = math.gcd(tempGCD, interval[i])

    for i in range(2, int(tempGCD**(1/2)) + 1):
        if tempGCD % i == 0:
            answer.append(i)
            answer.append(tempGCD//i)

    answer.append(tempGCD)
    return sorted(set(answer))




if __name__ == "__main__":
    N = int(sys.stdin.readline().rstrip())
    numbers = [int(sys.stdin.readline().rstrip()) for _ in range(N)]
    
    print(*solution(numbers))
    