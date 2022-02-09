import sys

def solution():
    minNum = min(num1, num2)
    maxNum = max(num1, num2)
    gcd, lcm = 0, 0
    for i in range(minNum, 0, -1):
        if num1 % i == 0 and num2 % i == 0:
            gcd = i
            break

    for i in range(1, minNum+1):
        if (maxNum * i) % minNum == 0:
            lcm = maxNum * i
            break
    
    return (gcd, lcm)

if __name__ == "__main__":
    num1, num2 = map(int, sys.stdin.readline().split())
    for i in solution():
        print(i)
    