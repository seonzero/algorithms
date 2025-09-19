#데이터의 개수
n = int(input())
m = int(input())
data = list(map(int, input().split()))

cnt = 0
interval_sum = 0
end = 0

#start를 차례대로 증가시킴
for start in range(n):
    #end를 가능한 만큼 이동시킨다
    while interval_sum < m and end < n:
        interval_sum += data[end]
        end+=1

    if interval_sum == m:
        cnt+=1

    interval_sum -= data[start]

print(count)