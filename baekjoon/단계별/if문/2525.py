import sys

def solution():
    hours = cookTime // 60
    minute = cookTime % 60

    if M+minute >= 60:
        hours += 1
        minute -= 60

    return ((H+hours) % 24, M+minute)

if __name__ == "__main__":
    H, M = map(int, sys.stdin.readline().split())
    cookTime = int(sys.stdin.readline().rstrip())
    
    for i in solution():
        print(i, end=" ")
    