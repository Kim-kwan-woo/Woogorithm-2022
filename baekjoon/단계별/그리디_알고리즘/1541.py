import sys

def solution(equation):
    equList = equation.split("-")
    answer = sum(map(int,equList[0].split("+")))
    for i in range(1, len(equList)):
        answer -= sum(map(int,equList[i].split("+")))

    return answer
        


if __name__ == "__main__":
    equation = sys.stdin.readline().rstrip()
    print(solution(equation))

