import sys

def solution(word):
    alpabet = [word[0]]

    for i in range(len(word)):
        if word[i] != alpabet[-1]:
            if word[i] in alpabet:
                return False
            else:
                alpabet.append(word[i])
        
    return True



if __name__ == "__main__":
    N = int(sys.stdin.readline().rstrip())
    count = 0
    for i in range(N):
        word = sys.stdin.readline().rstrip()
        if solution(word):
            count += 1

    print(count)
