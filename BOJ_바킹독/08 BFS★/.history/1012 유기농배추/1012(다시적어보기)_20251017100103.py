t = int(input())
dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(i, j):
    queue = [ (i,j) ]

    while queue:
        x,y = queue.pop(0)
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if matrix[nx][ny]==1:
                queue.append( (nx, ny) )
                matrix[nx][ny] == 0 #방문표시

for test_case in range(t):
    m,n,k=map(int, input().split())
    #배추밭만들기
    matrix = [ [0]*n for _ in range(m)]

    #배추좌표 받아서 밭에 표시하기
    for _ in range(k):
        y,x = map(int, input().split())
        matrix[x][y] = 1

    #배추밭 순회
    count = 0
    for i in range(n):
        for j in range(m):
            if matrix[i][j]==1:
                bfs(i,j)
                count +=1

    print(count)