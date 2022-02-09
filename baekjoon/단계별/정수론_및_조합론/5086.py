import sys

def solution():
    answer = []
    for i in numbers:
        num1 = i[0]
        num2 = i[1]
        if num2 % num1 == 0:
            answer.append("factor")
        elif num1 % num2 == 0:
            answer.append("multiple")
        else:
            answer.append("neither")
    
    return answer

    


if __name__ == "__main__":
    numbers = []
    while True:
        num1, num2 = map(int, sys.stdin.readline().split())
        if num1 == 0 and num2 == 0:
            break

        numbers.append([int(num1), int(num2)])
        
    for i in solution():
        print(i)

