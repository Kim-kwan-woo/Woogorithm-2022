import sys

def push(num):
    stack.append(num)

def pop():
    if not stack:
        print(-1)
    else:
        print(stack.pop())

def size():
    print(len(stack))

def empty():
    if not stack:
        print(1)
    else:
        print(0)

def top():
    if not stack:
        print(-1)
    else:
        print(stack[-1])



if __name__ == "__main__":
    N = int(sys.stdin.readline().rstrip())
    cmd = [list(sys.stdin.readline().split()) for _ in range(N)]

    stack = []
    for i in cmd:
        if i[0] == "push":
            push(int(i[1]))
        elif i[0] == "pop":
            pop()
        elif i[0] == "size":
            size()
        elif i[0] == "empty":
            empty()
        elif i[0] == "top":
            top()
    