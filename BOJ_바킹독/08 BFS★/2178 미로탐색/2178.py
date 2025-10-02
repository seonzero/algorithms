'''
4 6
101111
101010
101011
111011
'''
from collections import deque

n, m= map(int, input().split())

mrr = []
for _ in range(n):
    mrr.append(list(map(int, input())))

print(mrr)

dx = [-1, 0 , 1, 0]
dy = [0, 1, 0 ,-1]

def BFS(x, y):

    queue = deque()
    queue.append( (x, y) )

    while queue:
        #주어진 좌표에 대해서...
        x, y = queue.popleft()
        print()
        print(f'(x,y): {x}, {y}')

        #4방향 살펴보기
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            print()
            
            #★:(x,y) , ☆(nx, ny)
            for xx in range(n):
                for yy in range(m):
                    if xx==x and yy==y:
                        print('★', end=' ')
                    elif xx==nx and yy==ny:
                        print('☆', end= ' ')
                    else:
                        print(mrr[xx][yy], end=' ')
                print()
            

            #미로 범위 밖이면 
            if nx<0 or nx>=n or ny<0 or ny>=m:
                continue
            #길이 아니면
            if mrr[nx][ny]==0: 
                continue
            if mrr[nx][ny]==1:
                queue.append( (nx,ny) )
                mrr[nx][ny] = mrr[x][y]+1
                print('☆ 이 길로 갑니다')
            
            print()


    #들여쓰기 주의.queue에서 계산 다 하고나서 return 하는거임
    return mrr[n-1][m-1]
    
print(BFS(0,0))