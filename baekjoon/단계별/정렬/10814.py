import sys

def solution(people):
    count = 0
    for i in people:
        i.append(count)
        count+=1

    return sorted(people, key= lambda x: (int(x[0]), x[2]))


        

if __name__ == "__main__":
    N = int(sys.stdin.readline().rstrip())
    people = [list(sys.stdin.readline().split()) for _ in range(N)]

    for i in solution(people):
        print(i[0], i[1])