t = int(input())

dx = [-1, 1,0,0]
dy = [0,0,-1,1]

def bfs(x, y):
    queue = [ (x,y) ]
    matrix[x][y] = 0

    while queue:
        x,y = queue.pop(0)

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            #범위를 벗어나면 out(continue)
            if nx < 0 or nx>= m or ny < 0 or ny>=n:
                continue
            
            #배추라면... queue에 더해주고 방문표시(0)을 해준다
            if matrix[nx][ny]==1:
                queue.append( (nx, ny) ) #queue에 넣어준다. 
                matrix[nx][ny] = 0 #방문표시 (0)


for i in range(t):
    m,n,k = map(int, input().split())
    matrix = [ [0]*(n) for _ in range(m) ]
    cnt = 0

    #배추좌표 받기
    for j in range(k):
        x, y = map(int, input().split())
        matrix[x][y]=1

    #배추밭 살펴보기 - 하나씩
    for a in range(m):
        for b in range(n):
            #배추가 있으면 - 
            if matrix[a][b] == 1:
                bfs(a, b) 
                #배추가 있으면 cnt ++ 
                cnt += 1

    print(cnt)