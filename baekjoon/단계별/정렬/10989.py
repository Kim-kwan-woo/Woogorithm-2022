import sys

def solution(numList):
    #메모리가 초과 될 수 있기 때문에 계수 정렬 사용
    #숫자들의 개수를 카운트 하고 카운트 된 수 만큼 작은 수 부터 출력
    #입력 받은 수들의 배열을 생성하고 함수로 넘기는 것도 메모리를 차지하므로 메인함수에서 모두 구현
    return 0

        

if __name__ == "__main__":
    N = int(sys.stdin.readline().rstrip())
    count = [0 for _ in range(10001)]
    for i in range(N):
        number = int(sys.stdin.readline().rstrip())
        count[number] += 1

    for i in range(len(count)):
            if count[i] != 0:
                for j in range(count[i]):
                    print(i)