import sys

def solution(num):
    stack = []
    answer = []

    indexA, indexB = 0, 0
    sortedNum = sorted(num)

    while indexB != len(sortedNum):

        if stack and stack[-1] == num[indexA]:
            stack.pop()
            answer.append("-")
            indexA += 1
            continue

        stack.append(sortedNum[indexB])
        answer.append("+")
        indexB += 1

    for i in range(len(stack)-1, -1, -1):
        if stack[i] != num[indexA]:
            return ["NO"]
        else:
            answer.append("-")
            indexA += 1
    
    return answer

    
    

if __name__ == "__main__":
    n = int(sys.stdin.readline().rstrip())

    numbers = [int(sys.stdin.readline().rstrip()) for _ in range(n)]

    for i in solution(numbers):
        print(i)
    