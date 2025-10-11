from collections import deque

#(1) tmt 받기
m,n= map(int, input().split())

tmt = [list(map(int, input().split())) for _ in range(n)]

# print(tmt)
#(2) 우선 살펴보고
tmtbeing = 0 
for i in range(n):
    if 0 not in tmt[i]:
        tmtbeing += 1
    
#(2)-1. 다 익어있으면(0이 없으면) 0 출력하고 끝내기
if tmtbeing ==n :
    print('0')
#(3) 아니면 익은토마토(1)의 좌표를 queue에 넣어주고 
else: 
    queue = deque([])
    for i in range(n):
        for j in range(m):
            if tmt[i][j]==1:
                queue.append( (i, j) )
#(4) BFS를 돌리자 (토마토를 익혀준다 - 순회하고 방문처리해준다)
    while queue:
        x, y = queue.popleft()
        dx = [0,0,1,-1]
        dy = [-1,1,0,0]

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if (nx>=0) and (nx<n) and (ny>=0) and (ny<m):
                if tmt[nx][ny]==0:
                    queue.append( (nx, ny) )
                    tmt[nx][ny]= tmt[x][y]+1 #카운트는 이전 값에서 더해준다

# 0이 있는지는 다 살펴본다
#(5) 다 순회한 다음에 살펴본다 - 안익은게 잇으면(0) -1 출력, 아니면 count 출력하기
    res = 0
    for i in tmt:
        for j in i:
            if j==0:
                print(-1)
                exit(0)
        res = max(res, max(i))
    print(res-1)
