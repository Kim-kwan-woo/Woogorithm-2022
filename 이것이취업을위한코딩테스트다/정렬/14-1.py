import sys

#[baekjoon 10825 국영수]
#---answer---#
N = int(sys.stdin.readline().rstrip()) # 학생의 수
student = []

for i in range(N):
    data = sys.stdin.readline().split()
    student.append([data[0], int(data[1]), int(data[2]), int(data[3])])

student.sort(key=lambda x:(-x[1], x[2], -x[3], x[0]))

for i in student:
    print(i[0])

#---solution---#
# n = int(input())
# students = [] # 학생 정보를 담을 리스트

# # 모든 학생 정보를 입력받기
# for _ in range(n):
#     students.append(input().split())

# student.sort(key=lambda x: (-int(x[1]), int(x[2]), -int(x[3]), x[0]))

# # 정렬된 학생 정보에서 이름만 출력
# for student in students:
#     print(student[0])