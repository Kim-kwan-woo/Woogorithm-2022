import sys

#---answer---#
N = int(sys.stdin.readline().rstrip())

count = 0
for i in range(N+1):
    for j in range(60):
        for n in range(60):
            if '3' in str(i) or '3' in str(j) or '3' in str(n):
                count += 1

print(count)

#---solution---#
# # h를 입력받기
# h = int(input())

# count = 0
# for i in range(h+1):
#     for j in range(60):
#         for k in range(60):
#             if '3' in str(i) + str(j) + str(k):
#                 count += 1

# print(count)