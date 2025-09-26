import sys
from collections import deque 

input = sys.stdin.readline

n = int(input())
#배열이 아니라 덱이당
arr = deque( )
#(arr=[] - 배열로 선언한다)

for _ in range(n):
    comment = list(input().split())

    if comment[0] == 'push':
        arr.append(comment[1])
    elif comment[0] == 'pop':
        if arr:
            print(arr.pop(0))
        else: 
            print(-1)
    elif comment[0] == 'size':
        print(len(arr))
    elif comment[0]=='empty':
        if arr:
            print(0)
        else: 
            print(1)
    elif comment[0] == 'front':
        if arr:
            print(arr[0])
        else:
            print(-1)
    elif comment[0] == 'back':
        if arr:
            print(arr[-1])
        else:
            print(-1)