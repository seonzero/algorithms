'''
1 익은 토마토
0 안익은 토마토
-1 없음


<출력>
처음부터 모든 토마토가 익어있으면 - 0
ㄴ 0이 없다. 1과 -1로만 이루어져있다. < 를 어떻게 파악하지?
ㄴ 0 not in tomato: print(0) break

모두 못익히면 - 1
모두 익히면 - 며칠걸렸는지 출력
'''
from collections import deque 

def BFS(queue):
    print('bfs 함수 실행')
    dx = [-1,0,1,0]
    dy = [0,-1,0,1]


    while queue:
        x, y = queue.popleft()
        print('(x,y): {x}, {y}')

        #상하좌우 살피기
        for _ in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            #범위 내에서 0을 찾아서 떠나자
            if nx<0 or nx>=n or ny<0 or ny>=m:
                continue
            if tmt[nx][ny] == 1 or tmt[nx][ny]== -1:
                continue
            if tmt[nx][ny]==0:
                queue.append( (nx, ny) )
                tmt[nx][ny] = tmt[x][y] + 1

    return tmt


n, m = map(int, input().split())

tmt = []

for _ in range(m):
    tmt.append(list(map(int, input().split())))

print(tmt)
queue = deque()

for i in range(m):
    for j in range(n):
        if tmt[i][j] == 1:
            queue.append( (i, j) )
print(f'1들: {queue}') #여까지는 실행이 되는데 


if 0 not in tmt: # 이 아래로 안가짐 ㅜㅜ 
    print(f'none tmt')
    print(0)
else: 
    print('else')
    status = BFS(queue)
    if 0 in status:
        print(-1)
    else:
        print(max(status))
