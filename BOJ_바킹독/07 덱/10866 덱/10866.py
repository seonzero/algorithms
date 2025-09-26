#명령의 수 N (1 ≤ N ≤ 10,000)
import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
arr = deque( [] )

for _ in range(n):
    comm = list(input().split())
    c = comm[0]

    if c == 'push_front':
        arr.appendleft(comm[1])

    elif c == 'push_back':
        arr.append(comm[1])

    elif c == 'pop_front':
        if arr: 
            print(arr.popleft())
        else:
            print(-1)

    elif c=='pop_back':
        if arr:
            print(arr.pop())
        else: 
            print(-1)

    elif c=='size':
        print(len(arr))

    elif c=='empty':
        if arr: 
            print(0)
        else:
            print(1)

    elif c== 'front':
        if arr:
            print(arr[0])
        else:
            print(-1)

    elif c=='back':
        if arr:
            print(arr[-1])
        else: 
            print(-1)

    # print(arr)

    
