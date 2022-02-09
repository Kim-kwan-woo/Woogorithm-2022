import sys

def solution():
    factorial = 1
    count = 0

    for i in range(1, N+1):
        factorial *= i

    for i in range(len(str(factorial))-1, -1, -1):
        if str(factorial)[i] == "0":
            count += 1
        else:
            break
    return count

if __name__ == "__main__":
    N = int(sys.stdin.readline().rstrip())
    
    print(solution())
    