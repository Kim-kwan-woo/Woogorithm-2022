import sys

def solution(word):
    croatia = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]
    index = 0
    count = 0
    while True:
        findWord = word.find(croatia[index])
        if findWord != -1:
            count += 1
            word = word[:findWord] + ' ' + word[findWord+len(croatia[index]):]
        else:
            if index == len(croatia)-1:
                return count+len(word)-word.count(' ')
            index += 1

        if word == ' '*count:
            return count


if __name__ == "__main__":
    word = sys.stdin.readline().rstrip()
    print(solution(word))
