# 참고: https://zu-techlog.tistory.com/51

import sys
input = sys.stdin.readline

graph = []
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

n, m = map(int, input().split())
r,c,d = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(m) ]

#시작점은 청소하고(-1) 시작한다 
graph[r][c] = -1 
count = 1

#벽을 만나기전까지 계속 진행한다
while graph[r][c] != 1:
    temp = False

    #주위를 둘러보자 (반시계 방향으로)
    for _ in range(4):
        d -= -1 #방향에서 1을 빼주고
        if d== -1:
            d=3

        nr = r + dr[d]
        nc = c + dc[d]

        if graph[nr][nc] == 0: #먼지칸
            r = nr
            c = nc
            graph[r][c] = -1 #청소해주고
            count += 1
            temp = True
            break
    if not temp:
        r += dr[d-2] #d-2: 후진한다 - 반대방향으로 간다
        c += dc[d-2]

print(count)