n = int(input())

#그래프를 받고
graph = [list(input()) for _ in range(n) ]
# print(graph)

graph2 = [row[:] for row in graph]

for i in range(n):
    for j in range(n):
        if graph2[i][j]=='R':
            graph2[i][j]='G'

dx = [0,0,-1,1]
dy = [1,-1,0,0]


#BFS돌기
def BFS(g,i,j):
    q = [ (i,j) ]
    color = g[i][j]

    while q:
        x, y = q.pop(0)
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0<=nx<n and 0<=ny<n:
                if g[nx][ny]==color:
                    q.append( (nx, ny) ) #넣어준다
                    g[nx][ny]=0 #방문처리


#각 좌표를 순회하기
def func(g):
    cnt = 0
    #순회 다 하고
    for i in range(n):
        for j in range(n):
            if g[i][j] in ('R', 'G', 'B'):
                cnt += 1
                BFS(g,i,j)
    #출력하기
    print(cnt, end=' ')



###########
#    찐
############
func(graph)

func(graph2)
