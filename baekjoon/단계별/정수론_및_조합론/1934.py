import sys

def solution():
    # 먼저 유클리드 호제법으로 최대 공약수를 찾고
    # 두 수의 곱을 최대 공약수로 나누면 최소 공배수가 구해진다.
    # 유클리드 호제법(최대 공약수)
    # 1. 두 수에서 큰수를 작은수로 나눈다.
    # 2. 다시 작은 수였던 수를 1에서 나눈 나머지로 나눈다.
    # 3. 나눈 나머지가 0이 될때까지 반복한다. 
    # 4. 나눈 나머지가 0일때 작은 수였던 값이 최대 공약수 이다!!

    lcm = []
    for i in numbers:
        minNum = min(i[0], i[1])
        maxNum = max(i[0], i[1])

        #유클리드 호제법(최대 공약수)
        while minNum != 0:
            mod = maxNum % minNum
            maxNum = minNum
            minNum = mod
        gcd = maxNum

        #유클리드 호제법(최소 공배수)
        lcm.append((i[0]*i[1]) // gcd)
    
    return lcm

if __name__ == "__main__":
    T = int(sys.stdin.readline().rstrip())
    numbers = [list(map(int, sys.stdin.readline().split())) for _ in range(T)]
    
    for i in solution():
        print(i)
    