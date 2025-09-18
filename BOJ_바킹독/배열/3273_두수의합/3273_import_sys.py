# n개의 서로 다른 양의 정수로 이루어진 수열이 잇듬
# 자연수 x가 주어졌을 때 ai + aj = x를 만족하는 (ai, aj) 쌍의 수를 구하는 프로그램을 구해라

# 1 ≤ n ≤ 100000
import sys

n = int(sys.stdin.readline())
arr = set(map(int, sys.stdin.readline().split(" ")))
x = int(sys.stdin.readline())

count = 0
arr1 = arr[:len(arr)/2]
for ai in arr1 :
    aj = x- ai
    if aj in arr:
        count += 1
        # arr.remove(aj)

print(count)
