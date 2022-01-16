import sys
from math import pi

def solution(R):
    euclid = round(R**2 * pi, 6)
    taxi = "{:.6f}".format(float(2*R*R))

    print(euclid)
    print(taxi)


if __name__ == "__main__":
    R = int(sys.stdin.readline().rstrip())
    solution(R)
    