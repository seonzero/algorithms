# n개의 서로 다른 양의 정수로 이루어진 수열이 잇듬
# 자연수 x가 주어졌을 때 ai + aj = x를 만족하는 (ai, aj) 쌍의 수를 구하는 프로그램을 구해라

#(실패이유): (1 ≤ n ≤ 100000, 1 ≤ x ≤ 2000000) 임 숫자겁나큼
#시간초과
n = int(input())
arr = list(map(int, input().split()))
x = int(input())
count = 0

for ai in arr:
    aj = x- ai
    if aj in arr:
        count += 1
        arr.remove(aj)

print(count)
