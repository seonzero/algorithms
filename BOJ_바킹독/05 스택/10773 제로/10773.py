#잘못된 수를 부를 때마다 0을 외쳐서 가장 최근에 재민이가 쓴 수를 지우게 한다
#모든 수를 받아 적은 후, 그 수의 합을 알아내자
import sys
input = sys.stdin.readline

k = int(input())
arr = []

for _ in range(k):
    n = int(input())
    if n != 0:
        arr.append(n)
    else: 
        arr.pop()

print(sum(arr))