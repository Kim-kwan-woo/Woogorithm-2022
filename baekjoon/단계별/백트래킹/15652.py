import sys

def solution(numList, M, num):
    if M == 0:
        print(num)
    else:
        for i in range(len(numList)):
            if num == '':
                solution(numList[i:], M-1, str(numList[i]))
            else:
                solution(numList[i:], M-1, num +" "+ str(numList[i]))

            
        

if __name__ == "__main__":
    N, M = map(int,sys.stdin.readline().split())
    numList = [i for i in range(1, N+1)]
    solution(numList, M, '')