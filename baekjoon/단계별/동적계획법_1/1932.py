import sys

def solution(nums):
    for i in range(len(nums)-2, -1, -1):
        for j in range(len(nums[i])):
            nums[i][j] += max(nums[i+1][j], nums[i+1][j+1])

    return nums[0][0]
    
    

if __name__ == "__main__":
    N = int(sys.stdin.readline().rstrip())
    nums = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

    print(solution(nums))

