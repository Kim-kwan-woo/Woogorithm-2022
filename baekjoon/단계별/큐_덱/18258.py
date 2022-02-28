import sys
from collections import deque

def push(num):
    queue.append(num)

#pop이나 del연산을 사용하면 맨 앞의 원소를 삭제할 때
#모든 원소를 한칸씩 앞으로 옮겨야 하므로 시간이 오래 걸린다.
#따라서 deque를 사용하여 구현
def pop():
    if not queue:
        print(-1)
    else:
        print(queue.popleft())

def size():
    print(len(queue))

def empty():
    if not queue:
        print(1)
    else:
        print(0)

def front():
    if not queue:
        print(-1)
    else:
        print(queue[0])

def back():
    if not queue:
        print(-1)
    else:
        print(queue[-1])




if __name__ == "__main__":
    N = int(sys.stdin.readline().rstrip())
    cmd = [list(sys.stdin.readline().split()) for _ in range(N)]

    queue = deque([])
    for i in cmd:
        if i[0] == "push":
            push(int(i[1]))
        elif i[0] == "pop":
            pop()
        elif i[0] == "size":
            size()
        elif i[0] == "empty":
            empty()
        elif i[0] == "front":
            front()
        elif i[0] == "back":
            back()
    