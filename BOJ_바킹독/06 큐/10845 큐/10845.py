import sys
input = sys.stdin.readline

n = int(input())
arr = []

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