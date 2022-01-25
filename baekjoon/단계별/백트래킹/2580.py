import sys

def solution(count):
    if count == len(zero):
        for i in range(9):
            #리스트 앞에 *을 쓰면 모든 원소가 공백으로 구분되어 문자열 형태로 출력된다.
            print(*sudoku[i])
        # 답이 여러개가 나올 수 있으므로 return이 아닌 exit를 사용하여 하나의 답만 출력 후 프로그램 종료
        exit(0)

    for i in range(1, 10):
        x = zero[count][0]
        y = zero[count][1]

        if checkRow(x, i) and checkCol(y, i) and checkRect(x, y, i):
            sudoku[x][y] = i
            solution(count+1)
            #백트래킹(다른 경로의 값들을 위해 값을 초기화 해주어야 한다.)
            sudoku[x][y] = 0 

def checkRow(x, num):
    for i in range(9):
        if num == sudoku[x][i]:
            return False
    return True

def checkCol(y, num):
    for i in range(9):
        if num == sudoku[i][y]:
            return False
    return True

def checkRect(x, y, num):
    tempX = x // 3 * 3
    tempY = y // 3 * 3
    for i in range(tempX, tempX + 3):
        for j in range(tempY, tempY + 3):
            if num == sudoku[i][j]:
                return False
    return True


if __name__ == "__main__":
    sudoku = [list(map(int,sys.stdin.readline().split())) for _ in range(9)]

    zero = []
    for i in range(9):
        for j in range(9):
            if sudoku[i][j] == 0:
                zero.append((i, j))

    solution(0)