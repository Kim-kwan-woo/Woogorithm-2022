import sys

def d(n):
    return n + sum(list(map(int, str(n))))

if __name__ == "__main__":
    nonSelfNumber = []
    for i in range(1, 10000):
        num = d(i)
        if num <= 10000:
            nonSelfNumber.append(num)
    
    selfNumber = sorted({i for i in range(1, 10000)} - set(nonSelfNumber))

    for i in selfNumber:
        print(i)