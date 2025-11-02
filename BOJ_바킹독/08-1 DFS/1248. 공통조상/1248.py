tc = int(input())

for t in range(tc):
    #정점개수v, 간선개수e
    v,e,x,y = map(int, input().split())
    #1 2 1 3 2 4 3 5 3 6 4 7 7 12 5 9 5 8 6 10 6 11 11 13 (총 2*e개의 숫자)
    nodes = list(map(int, input().split()))
    #인접리스트
    graph = [ [] for _ in range(v+1) ]

    for i in range(e):
        graph[nodes[2*i]].append(nodes[2*i+1])


    def find_child(x, childs):
        for i in range(v+1):
            if x in graph[i]:
                childs.append(i)
                find_child(i, childs)
        return childs
    
    child1 = find_child(x, childs=[])
    child2 = find_child(y, childs=[])
    # print(child1)
    # print(child2)

    #2. 공통조상 찾기
    if len(child1)<len(child2):
        short = child1
        long=child2
    else:
        short = child2
        long = child1

    found = False
    for s in short:
        for i in long: 
            if i==s:
                root = i
                found = True
                # print(f'root: {root}')
                break
        if found:
            break

    
    cnt = 0
    #3. 서브트리 count
    def count_child(r): #3번받으면
        global cnt
        cnt+=1
        # print(f'now: {r}, child: {graph[r]}, cnt: {cnt}')

        
        if graph[r]: #[5,6]
            for i in graph[r]:
                count_child(i) #5를 넣어주고 - 6을 넣어주고
        else:
            pass

    cnt = 0
    count_child(root)
    print(f'#{t+1} {root} {cnt}')