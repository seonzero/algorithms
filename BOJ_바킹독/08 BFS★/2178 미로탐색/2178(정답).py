'''
참조: https://velog.io/@ssulee0206/%EB%B0%B1%EC%A4%80-2178%EB%B2%88-%EB%AF%B8%EB%A1%9C%ED%83%90%EC%83%89%ED%8C%8C%EC%9D%B4%EC%8D%AC
'''

from collections import deque

n, m = map(int, input().split() )
mrr = []
for _ in range(n):
    mrr.append(list(map(int, input())))

def BFS(x, y):
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]

    queue = deque()
    queue.append((x, y))

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx<0 or nx>=n or ny<0 or ny>=m:
                continue
            if mrr[nx][ny]==0:
                continue
            if mrr[nx][ny]==1:
                mrr[nx][ny] = mrr[x][y] + 1
                queue.append( (nx, ny) )

    return mrr[n-1][m-1]

print(BFS(0,0))