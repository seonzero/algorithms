#cnt_v:현재 탐색 중인 정점
def dfs(cnt_v, adj_matrix, visited):
    #방문표시해주기
    visited[cnt_v] = True

    #인접 정점들
    adj_list = adj_matrix[cnt_v]

    #cnt_v와 인접한 정점에 대해서 방문하자
    for i in range(len(adj_list)):
        #조건: 인접하고, 방문한 적이 없는 경우에만 dfs를 실행한다
        if adj_matrix[cnt_v][i] and not visited[i] 
            dfs(i, adj_matrix, visited)

n = int(input()) #5라고 가정
adj_matrix = [
    [0,1,1,0,0],
    [1,0,0,1,1],
    [1,0,0,0,1],
    [0,1,1,1,0]
]

#방문처리관리변수 
#맨 처음에는 아직 모든 정점들에 대해서 방문하지 않았음. 
visited = [False] * n

#그래프는 모든 정점이 서로 연결되지 않을 수도 있다. 
#분리된 그래프의 존재 가능성
#모든 정점에서 DFS를 실행하자
for i in range(n):
    #방문한 적이 있다면 DFS를 실행하지 않는다
    if visited[i]: continue

    #시작정점을 0으로 시작
    dfs(start=0, adj_matrix, visited)