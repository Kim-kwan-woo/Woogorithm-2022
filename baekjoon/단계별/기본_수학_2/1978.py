import sys

def solution(nums):
    count = 0
    for i in nums:
        check = True if i != 1 else False
        for j in range(2, i):
            if i % j == 0:
                check = False
                break
        
        if check:
            count += 1

    return count
    

    
if __name__ == "__main__":
    N = int(sys.stdin.readline().rstrip())
    nums = list(map(int, sys.stdin.readline().split()))
    print(solution(nums))