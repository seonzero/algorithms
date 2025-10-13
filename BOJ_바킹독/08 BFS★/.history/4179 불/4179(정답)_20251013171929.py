# 참고링크: https://velog.io/@hygge/Python-%EB%B0%B1%EC%A4%80-4179-%EB%B6%88-BFS
import sys
from collections import deque
imput = sys.stdin.readline

n,m = map(int, input().split())
graph = []

# 지훈이는 0
for i in range(n):
    graph.append(list(input().rstrip()))
    if 'J' in graph[i]:
        q = deque( [ (0,i, graph[i].index('J') )]) 

#불은 -1로 표시한다 !!
for i in range(n):
    for j in range(m):
        if graph[i][j] == 'F':
            q.append( (-1, i , j) ) 

dx = [-1,1,0,0]
dy = [0,0,1,-1]
ans = 'IMPOSSIBLE'


# 불이야~!!
while q:
    time, x, y = q.popleft()

    #지훈이 탈출 조건
    #불이 아니고, 다음 길이 불로 덮이지 않았고, 모서리에 위치하면...
    if time > -1 and graph[x][y]!='F' and (x==0 or y==0 or x==n-1 or y==m-1):
        ans==time + 1
        break
    
    #순회하자
    for i in range(4):
        nx = x + dx[i]
        ny = y + dx[i]

        #벽도 아니고 미로 내부에 존재한다면
        if 0<=nx<=n and 0<=ny<m and graph[nx][ny] != '#':
            #지훈이 이동 (time이 -1보다 크다: 지훈이다)
            if time > -1 and graph[nx][ny] == '.':
                # 흔적(_)만 남겨준다 - 왔던 길을 되돌아 가지 않도록
                graph[nx][ny] = '_'
                q.append( (time+1, nx, ny ) )

            #불 퍼뜨리기
            elif time == -1 and graph[nx][ny] != 'F':
                graph[nx][ny] = 'F'
                q.append( (-1, nx, ny ) )

print(ans)