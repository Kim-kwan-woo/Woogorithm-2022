import sys

def solution(word):
    time = 0
    for i in word:
        if i == 'A' or i == 'B' or i == 'C':
            time += 3
        elif i == 'D' or i == 'E' or i == 'F':
            time += 4
        elif i == 'G' or i == 'H' or i == 'I':
            time += 5
        elif i == 'J' or i == 'K' or i == 'L':
            time += 6
        elif i == 'M' or i == 'N' or i == 'O':
            time += 7
        elif i == 'P' or i == 'Q' or i == 'R' or i == 'S':
            time += 8
        elif i == 'T' or i == 'U' or i == 'V':
            time += 9
        else:
            time += 10

    return time

if __name__ == "__main__":
    word = sys.stdin.readline().rstrip()
    
    print(solution(word))