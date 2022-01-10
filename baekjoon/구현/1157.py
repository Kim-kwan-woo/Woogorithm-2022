import sys
import operator
def solution(string):
    alphabet = {"A":0, "B":0, "C":0, "D":0, "E":0, "F":0, "G":0, 
    "H":0, "I":0, "J":0, "K":0, "L":0, "M":0, "N":0, "O":0, 
    "P":0, "Q":0, "R":0, "S":0, "T":0, "U":0, "V":0, "W":0, 
    "X":0, "Y":0, "Z":0}

    upperStr = string.upper()

    for i in upperStr:
        alphabet[i] += 1

    tempdict = sorted(alphabet.items(), key=operator.itemgetter(1), reverse=True)

    if tempdict[0][1] == tempdict[1][1]:
        return "?"
    else:
        return tempdict[0][0]

if __name__ == "__main__":
    string = sys.stdin.readline().rstrip()
    
    print(solution(string))