from collections import deque

n, k = map(int, input().split())
q = deque([(n, 0)])
visited = set([n]) #방문한 노드 저장 - 우선 n은 방문해줌
if n==k:
    print(0)
else:
    while q:
        x, count = q.popleft()

        # if k in (x-1, 2*x, x+1):
        #     print(count+1)
        #     break
        
        # if (x-1) not in lst: #연산해본적이없다
        #     q.append( (x-1, count+1) )
        #     lst.append(x-1)
        # if (2*x) not in lst:
        #     q.append( (2*x, count+1) )
        #     lst.append(2*x)
        # if (x+1) not in lst:
        #     q.append( (x+1, count+1) )
        #     lst.append(x+1)


        #세 가지 경우를 for문을 이용해 살펴본다. 
        #조건에 맞는게 나오면 탈출시키고
        #아니면 다른 조건을 검토하고 - 넣는다. 
        for nx in (x-1, 2*x, x+1):
            if nx==k:
                print(count+1)
                exit()
            if 0 <= nx <= 100000 and nx not in visited:
                visited.add(nx)
                q.append( (nx, count+1) )