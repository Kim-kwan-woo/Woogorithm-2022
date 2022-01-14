import sys

def solution(x, y):
    distance = y - x
    move = 0
    i = 1

    while distance > move:
        if distance > move:
            move += 2*i

        if distance < move:
            move -= 2*i
            break

        if distance == move:
            return i*2
            
        i += 1

    if distance - move > i:
        return (i-1)*2+2
    else:
        return (i-1)*2+1
    
    
if __name__ == "__main__":
    T = int(sys.stdin.readline().rstrip())
    answer = []
    for i in range(T):
        x, y = map(int, sys.stdin.readline().split())
        answer.append(solution(x, y))

    for i in answer:
        print(i)