import sys

def solution(string):
    if len(string) == 0:
        return 0
    elif string[0] == " ":
        string = string[1:]
    elif string[-1] == " ":
        string = string[:-1]

    return len(string.split(' '))

if __name__ == "__main__":
    string = sys.stdin.readline().rstrip()
    
    print(solution(string))