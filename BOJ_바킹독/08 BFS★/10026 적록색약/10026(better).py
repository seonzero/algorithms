from collections import deque

def BFS(x,y):
    q.append( (x,y) )
    dx = [0,0,-1,1]
    dy = [1,-1,0,0]
    visited[x][y] = 1
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<n and 0<=ny<n and graph[nx][ny] == graph[x][y] and not visited[nx][ny]:
                visited[nx][ny] = 1
                q.append( (nx, ny) )

n = int(input())
graph = [list(input()) for _ in range(n) ]
q=deque()

visited = [[0]*n for _ in range(n)]
cnt1=0
for i in range(n):
    for j in range(n):
        if not visited[i][j]: 
            BFS(i, j)
            cnt1 += 1


visited = [[0]*n for _ in range(n)]
cnt2 = 0
for i in range(n):
    for j in range(n):
        if graph[i][j]=='R':
            graph[i][j]='G'

for i in range(n):
    for j in range(n):
        if not visited[i][j]: 
            BFS(i, j)
            cnt2 += 1

print(cnt1, cnt2)