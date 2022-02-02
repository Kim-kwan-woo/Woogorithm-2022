import sys

def solution():
    answer = [nums[0]]
    for i in range(1, n):
        if answer[i-1] > 0:
            answer.append(answer[i-1]+nums[i])
        else:
            answer.append(nums[i])

    return max(answer)

    



if __name__ == "__main__":
    n = int(sys.stdin.readline().rstrip())
    nums = list(map(int, sys.stdin.readline().split()))

    print(solution())

