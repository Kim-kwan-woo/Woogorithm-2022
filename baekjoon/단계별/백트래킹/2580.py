import sys

def solution():
    #가로 비교
    for i in range(9):
        if sudoku[i].count(0) == 1:
            index = 0
            numList = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
            for j in range(9):
                numList.remove(sudoku[i][j])
                if sudoku[i][j] == 0:
                    index = j

            sudoku[i][index] = numList[0]

    #세로 비교(아직 안했음)
    for i in range(9):
        if sudoku[i][i].count(0) == 1:
            index = 0
            numList = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
            for j in range(9):
                numList.remove(sudoku[i][j])
                if sudoku[i][j] == 0:
                    index = j

            sudoku[i][index] = numList[0]
            



        

if __name__ == "__main__":
    #이거 스도쿠 1차원 배열로 해봐야겠다.
    sudoku = [list(map(int,sys.stdin.readline().split())) for _ in range(9)]
    solution()
    for i in range(9):
        print()
        for j in range(9):
            print(sudoku[i][j], end=' ')