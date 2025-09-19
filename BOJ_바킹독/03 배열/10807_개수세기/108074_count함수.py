#배열 속 숫자 v가 몇개 포함되어있는지 알아보자 
#배열은 최대 100개의 숫자

n = int(input())
arr = list(map(int, input().split()))
v = int(input())

# count=0
# for i in arr:
#     if v==i:
#         count += 1
print(arr.count(v))