import sys

def solution():
    answer = []
    for i in pare:
        stk = []
        tempList = list(i)
        for j in tempList:
            if j == "(":
                stk.append(j)
            else:
                if not stk:
                    stk.append(j)
                    break

                if stk[-1] == "(":
                    stk.pop()
                else:
                    answer.append("NO")
                    break
        
        if stk:
            answer.append("NO")
        else:
            answer.append("YES")

    return answer

if __name__ == "__main__":
    T = int(sys.stdin.readline().rstrip())
    pare = [sys.stdin.readline().rstrip() for _ in range(T)]

    for i in solution():
        print(i)
    