'''#LCA 공통조상
- 깃 두 브랜치의 공통 조상을 찾을 때
- 네트워크에서 '라우팅' 경로 최적화할 때
- 디렉토리 공통 상위 디렉토리를 찾을 때

1. 각 노드의 부모노드, 깊이, 서브트리를 미리 구해다 놓는다 (DFS)
2. 우리가 구하고 싶은 노드들의 깊이를 맞춘다
3. 서로 부모로 올라가면서 같은 값인지 비교하고 - 같으면 걔는 공통조상이다. 

'''

def dfs(node, depth):
    #해당 접근 노드의 깊이를 저장
    depths[node] = depth 

    #방문하지 않은 노드들을 dfs로 방문하자
    for child in tree[node]:
        #부모정보 저장해주기
        parent[child] = node 
        #자식노드에 대해 dfs실행 - depth+1을 전달해줌
        dfs(child, depth+1)

    ###############################
    #코드가 이쪽에 도달했다는 의미는?
    #위의 for문 코드가 다 실행됐다 
    #더이상 진행할(내려갈) 곳이 없다는 의미

    #서브트리 크기에 본인 노드를 포함시킨 다음에
    size[node] = 1
    #리프노드가 왔다면, 자식이 없기 때문에 서브트리 개수는 1로 설정되고 끝난다. 
    for child in tree[node]:
        size[node] += size[child]

def LCA(a, b):
    while depths[a] != depths[b]:
        if depths[a] > depths[b]: #a가 더 깊이 있다. 
            a = parent[a] #a를 a의 부모로 바꾼다 
        else:
            b = parent[b] #b를 b의 부모로 바꾼다. 

    #a와 b가 같으면 - 공통 조상인거고
    #다르면 둘다 부모로 한 칸씩 올라간다!
    while a!=b:
        a=parent[a]
        b=parent[b]

    return a


tc = int(input())
for t in range(1, tc+1):
    v,e,a,b, = map(int, input().split())
    edges = list(map(int, input().split()))

    # 0. 트리 구성하기
    tree = [ [] for _ in range(v+1)]

    for i in range(e):
        tree[edges[2*i]].append(edges[2*i+1])

    #why: 부모의 정점 번호를 인덱스로 활용할 것. 
    #각 노드의 부모노드 저장해두기 (부모노드를 찾아서 올라가기 위해서)
    parent = [0] * (v+1)

    #각 노드의 길이를 저장하기 (공통조상을 찾기 위한 두 노드의 깊이를 맞추기 위해서!)
    depths = [0] * (v+1)

    #각 노드의 서브트리 크기를 저장할 변수
    size = [0] * (v+1)

    #dfs를 수행하면서, 트리를 탐색하면서 모든 노드의 부모/깊이/서브트리의 크기를 구한다. 
    dfs(1,0) #정점1에서 시작할 것. 깊이는 0이라는 뜻

    common = LCA(a,b)
    print(f'#{t} {common} {size[common]}')