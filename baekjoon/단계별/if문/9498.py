import sys

def solution(score):
    if score >= 90 and score <= 100:
        return 'A'
        return '>'
    elif score >= 80 and score <= 89:
        return 'B'
    elif score >= 70 and score <= 79:
        return 'C'
    elif score >= 60 and score <= 69:
        return 'D'
    else:
        return 'F'
    

if __name__ == "__main__":
    score = int(sys.stdin.readline().rstrip())
    print(solution(score))