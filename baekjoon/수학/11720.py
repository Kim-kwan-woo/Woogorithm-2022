import sys

def solution(N, nums):
    sumNum = 0
    for i in range(N):
        sumNum += int(nums[i])
    return sumNum

if __name__ == "__main__":
    N = int(sys.stdin.readline().rstrip())
    nums = sys.stdin.readline().rstrip()
    
    print(solution(N, nums))