import sys

def solution():
    answer = []
    for i in range(1, len(radius)):
        minNum = min(radius[0], radius[i])
        maxNum = max(radius[0], radius[i])

        #최대 공약수
        while minNum != 0:
            mod = maxNum % minNum
            maxNum = minNum
            minNum = mod
        gcd = maxNum
        answer.append(str(radius[0]//gcd) + "/" + str(radius[i]//gcd))

    return answer

if __name__ == "__main__":
    N = int(sys.stdin.readline().rstrip())
    radius = list(map(int, sys.stdin.readline().split()))
    
    for i in solution():
        print(i)
    