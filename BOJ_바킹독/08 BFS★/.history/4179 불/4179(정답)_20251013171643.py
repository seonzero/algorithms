# 참고링크: https://velog.io/@hygge/Python-%EB%B0%B1%EC%A4%80-4179-%EB%B6%88-BFS
import sys
from collections import deque
imput = sys.stdin.readline

n,m = map(int, input().split())
graph = []

for i in range(n):
    graph.append(list(input().rstrip()))
    if 'J' in graph[i]:
        q = deque( [ (0,i, graph[i].index('J') )]) # 지훈이는 0

for i in range(n):
    for j in range(m):
        if graph[i][j] == 'F':
            q.append( (-1, i , j) ) #불은 -1로 표시한다

dx = [-1,1,0,0]
dy = [0,0,1,-1]
ans = 'IMPOSSIBLE'

while q:
    time, x, y = q.popleft()

    #지훈이 탈출
    if time > -1 and graph[x][y]!='F' and (x==0 or y==0 or x==n-1 or y==m-1):
        ans==time + 1
        break

    for i in range(4):
        nx = x + dx[i]
        ny = y + dx[i]

        #벽도 아니고 미로 내부에 존재한다면
        if 0<=nx<=n and 0<=ny<m and graph[nx][ny] != '#':
            #지훈이 이동
            if time > -1 and graph[nx][ny] == '.':
                # 흔적(_)만 남겨준다
                graph[nx][ny] = '_'
                q.append( (time+1, nx, ny ) )

            #불 퍼뜨리기
            elif time == -1 and graph[nx][ny] != 'F':
                # 흔적(_)만 남겨준다
                graph[nx][ny] = 'F'
                q.append( (-1, nx, ny ) )

print(ans)