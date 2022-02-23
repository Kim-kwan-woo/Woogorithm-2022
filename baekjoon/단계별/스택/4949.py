import sys

def solution(string):
    stack = []
    for i in string:
        if i == "(" or i == "[":
            stack.append(i)
        elif i == ")":
            if not stack:
                return "no"

            if stack[-1] == "(":
                stack.pop()
            else:
                return "no"
        elif i == "]":
            if not stack:
                return "no"
                
            if stack[-1] == "[":
                stack.pop()
            else:
                return "no"

    if not stack:
        return "yes"
    else:
        return "no"

if __name__ == "__main__":
    answer = []
    while True:
        string = list(sys.stdin.readline().rstrip())

        if string[0] == ".":
            break
        
        answer.append(solution(string))

    for i in answer:
        print(i)

    