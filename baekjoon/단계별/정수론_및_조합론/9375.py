import sys

def solution():
    count = 1
    for n in clothes:
        count *= (len(clothes[n]) + 1)
    
    return count - 1

    




if __name__ == "__main__":
    T = int(sys.stdin.readline().rstrip())
    
    answer = []
    for i in range(T):
        n = int(sys.stdin.readline().rstrip())
        clothes = {}

        for j in range(n):
            item, cate = sys.stdin.readline().split()
            if not cate in clothes:
                clothes[cate] = [item]
            else:
                clothes[cate].append(item)
        
        answer.append(solution())

    for i in answer:
        print(i)
    