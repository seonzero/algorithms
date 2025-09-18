n, k = map(int, input().split())

students = [ [0,0] for _ in range(7) ]

for _ in range(n):
    gender, grade = map(int, input().split())
    students[grade][gender] += 1

room = 0


for grade in students:
    for num in grade: #<- 이렇게하면 바로 순환 가능 ㅋ
        room += num // k
        if num % k:
            room +=1 

print(room)