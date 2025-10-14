from collections import deque

test_case = int(input())
m,n,k = map(int, input().split())

#배추밭 만들기
graph = [[0]*n]*m

print(graph)


#배추좌표 받기
q= deque()
for _ in range(k):
    x,y = map( int, input().split() ) 
    graph[x-1][y-1] = 1
    q.append( (x,y) )