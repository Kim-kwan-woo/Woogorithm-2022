import sys

def solution(R, S):
    newStr = ""
    for i in S:
        newStr += i*R

    return newStr

if __name__ == "__main__":
    T = int(sys.stdin.readline().rstrip())
    answer = []
    for i in range(T):
        R, S = sys.stdin.readline().split()
        answer.append(solution(int(R), S))
    
    for i in answer:
        print(i)