def dfs(start_vertex, visited, graph, result):
    #0. 방문 여부를 체크한다
    visited.add(start_vertex) #set은 add를 넣어준다.
    result.append(adj_v)

    #1@정점이 없는 그래프일수도 있다!
    #인접그래프 없으면 미리 return 시키기
    if start_vertex not in graph:
        return
    
    #1. 인접 정점 정보들을 받는다
    adj_list = graph[start_vertex]


    #2 그 인접 정점 중 조건을 확인한다
    #조건: 방문여부
    for adj_v in adj_list:
        #방문한 정점이면 continue(skip)
        if adj_v in visited:
            continue
        #방문안했으면 진행하기 
        dfs(adj_v, visited, graph, result)

    #3. 방문한다 - 방문여부체크 및 DFS 실행


#그래프 인접리스트
#@: A에서 B로 갔는데 - B는 인접 정보가 없는 경우 - 1번이 터짐
#그래서 미리미리 이런 경우도 생각해서 조건문으로 막아줘야한다. 
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'G'],
    'D': ['B', 'F'],
    'E': ['B', 'F'], 
    'F': ['D', 'E', 'G'],
    'G': ['C', 'F']
}

start_vertex = 'A'
visited = set() #set()이 무슨 의미지?? 
'''
방문처리변수방법
1. [False] * n
2. 빈세트를 만들고 방문할 때마다 넣어준다 
- in 연산자를 써서 여기에 들어있는지 알아보기
~ 이게 문제를 더 유연하게 풀 수 있다. 
'''
result = []

dfs(start_vertex, visited, graph)

print(' '.join(result))