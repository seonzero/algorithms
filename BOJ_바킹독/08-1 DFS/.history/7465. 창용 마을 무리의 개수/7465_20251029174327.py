def DFS(near, visited, edges):
    # print(f'{near}에 가볼게요')
    #방문한 적 있으면 skip
    if near in visited:
        # print('방문한적있음')
        return
    
    #방문 여부 등록
    visited.add(near)
    # print(f'visited: {visited}')

    #인접리스트 정보 받기
    adj_list = edges[near]
    # print(f'{near}의 인접리스트는 {adj_list}입니다!')
    for adj in adj_list:
        # print(f'인접리스트 살피러갑니다')
        DFS(adj, visited, edges)

tc = int(input())

for t in range(tc):
    #노드개수n, 간선개수m
    n, m = map(int, input().split())
    
    #간선정보
    edges = [ [] for _ in range(n+1)]
    for _ in range(m):
        start, end = map(int, input().split())
        #인접리스트 'start': ['end'] <- 이렇게 넣고싶음.
        #이차원 배열을 이용해서 구현한다 (파이썬)
        edges[start].append(end)
        edges[end].append(start)

    # print(f'edge: {edges}')

    #방문정보 저장
    visited = set()
    cnt = 0

    #모든 정점들을 돌아보자
    for i in range(1, n+1):
       if i not in visited:
        # print(f'@@ 방문할 접점: {i}')
        cnt += 1
        DFS(i, visited, edges)
        # print('@@')


print(cnt)