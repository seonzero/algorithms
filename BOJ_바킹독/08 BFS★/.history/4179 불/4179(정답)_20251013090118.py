import sys
from collections import deque
imput = sys.stdin.readline

n,m = map(int, input().split())
graph = []

for i in range(n):
    graph.append(list(input().rstrip()))
    if 'J' in graph[i]:
        q = deque( [ (0,i, graph[i].index('J') )]) # 지훈이는 0

for i in range(n):
    for j in range(m):
        if graph[i][j] == 'F':
            q.append( (-1, i , j) ) #불은 -1로 표시한다

dx = [-1,1,0,0]
dy = [0,0,1,-1]
ans = 'IMPOSSIBLE'

while q:
    
