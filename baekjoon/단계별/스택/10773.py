import sys

def solution():
    stack = []
    for i in nums:
        if i != 0:
            stack.append(i)
        else:
            stack.pop()

    return sum(stack)

if __name__ == "__main__":
    K = int(sys.stdin.readline().rstrip())
    nums = [int(sys.stdin.readline().rstrip()) for _ in range(K)]

    print(solution())
    