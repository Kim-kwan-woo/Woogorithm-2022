import sys

def solution(N):
    minNum = sys.maxsize
    for i in startTeam:
        startScore = 0
        linkScore = 0
        people = [k for k in range(N)]
        for j in range(N//2):
            for n in range(j+1, N//2):
                startScore += S[i[j]][i[n]] + S[i[n]][i[j]]
            people.remove(i[j])

        for j in range(N//2):
            for n in range(j+1, N//2):
                linkScore += S[people[j]][people[n]] + S[people[n]][people[j]]

        if abs(startScore - linkScore) < minNum:
            minNum = abs(startScore - linkScore) 

    return minNum

    

def makeTeam(N, total, num, step):
    if step == N//2:
        startTeam.append(list(map(int,total.split())))
    else:
        for i in range(num+1, N):
            makeTeam(N, total + ' ' + str(i), i, step+1)

if __name__ == "__main__":
    N = int(sys.stdin.readline().rstrip()) 
    S = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
    
    startTeam = []
    makeTeam(N, '', -1, 0)
    print(solution(N))