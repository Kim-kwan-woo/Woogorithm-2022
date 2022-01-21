import sys

def solution(num, index):
    if index == len(nums):
        answer.append(num)
    else:
        for j in range(4):
            if operators[j] != 0:
                operators[j] -= 1
                if j == 0: #더하기
                    solution(num+nums[index], index+1)
                elif j == 1: #빼기
                    solution(num-nums[index], index+1)
                elif j == 2: #곱하기
                    solution(num*nums[index], index+1)
                else: #나누기
                    if num < 0:
                        solution(-(abs(num)//nums[index]), index+1)
                    else:
                        solution(num//nums[index], index+1)
                operators[j] += 1
        

if __name__ == "__main__":
    N = int(sys.stdin.readline().rstrip()) 
    nums = list(map(int,sys.stdin.readline().split()))
    operators = list(map(int,sys.stdin.readline().split()))
    answer = []
    solution(nums[0], 1)
    print(max(answer))
    print(min(answer))
