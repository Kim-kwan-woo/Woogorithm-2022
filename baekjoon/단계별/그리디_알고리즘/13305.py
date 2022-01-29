import sys

def solution():
    minCost = min(cost[:-1])
    totalCost = 0
    tempCost = cost[0]
    for i in range(len(cost)-1):
        if cost[i] != minCost:
            if tempCost > cost[i]:
                tempCost = cost[i]
            totalCost += tempCost*distance[i]
        else:
            totalCost += cost[i]*sum(distance[i:])
            break
    
    return totalCost

        


if __name__ == "__main__":
    N = int(sys.stdin.readline().rstrip())
    distance = list(map(int, sys.stdin.readline().split()))
    cost = list(map(int, sys.stdin.readline().split()))
    print(solution())

