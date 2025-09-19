#1학년-6학년
#한 방에는 남남, 여여, 같은학년끼리
#한 방에 한 명도 가능
#한 방에 배정가능한 최대인원후 k
#조건에맞게학생을배정하기위한방의 최소개수

#참가학생수:n, 배정최대인원수:k
# 첫 번째 줄에는 수학여행에 참가하는 학생 수를 나타내는 정수 N(1 ≤ N ≤ 1,000)과 
# 한 방에 배정할 수 있는 최대 인원 수 K(1 < K ≤ 1,000)
n, k = map(int, input().split())

#학생의 성별 s(여0 남1), 학년y
students = [ [0,0] for _ in range(7) ]
# print(students)

for _ in range(n):
    gender, grade = map(int, input().split())
    students[grade][gender] += 1

# print(students)
room = 0

for g in range(1, 7): #123456
    for s in range(2): #01
        personnel = students[g][s]
        # print(f'grade: {g}, gender: {s}, 인원: {personnel}')
        if personnel == 0:
            continue
        #지정된 인원수보다 많다
        elif personnel > k:
            room += personnel//k
            if personnel%k!=0:
                room += 1
        else: 
            room+=1

print(room)