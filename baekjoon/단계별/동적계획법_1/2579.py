import sys

def solution(stairs):
    if len(stairs) < 3:
        return sum(stairs)
        
    stairs[-2] += stairs[-1]
    oneStep = True
    for i in range(len(stairs)-3, -1, -1):
        if oneStep:
            stairs[i] += stairs[i+2]
            oneStep = False
        else:
            if stairs[i+1] > stairs[i+2]:
                stairs[i] += stairs[i+1]
                oneStep = True
            else:
                stairs[i] += stairs[i+2]

    return (stairs[0], stairs[1])

    
    

if __name__ == "__main__":
    N = int(sys.stdin.readline().rstrip())
    stairs = [int(sys.stdin.readline().rstrip()) for _ in range(N)]

    print(solution(stairs))

