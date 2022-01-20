import sys

def solution(N):
    title = 665
    count = 0
    while count < N:
        title += 1
        if str(title).find('666') != -1:
            count += 1
        
    return title

        

if __name__ == "__main__":
    N= int(sys.stdin.readline().rstrip())
    print(solution(N))

