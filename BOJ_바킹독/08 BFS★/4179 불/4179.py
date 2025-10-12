from collections import deque

r,c = map(int, input().split())
mirr = [ list(input()) for _ in range(r) ]
print(mirr)

queue = deque([])
#J와 F의 좌표 받기
for i in range(r):
    for j in range(c):
        if mirr[i][j]=='J':
            queue.append( (i,j,'J') )
            mirr[i][j] = 1
        elif mirr[i][j]=='F':
            queue.append( (i,j,'F') )


#각각 탐색해보기
dx = [0,0,1,-1]
dy = [1,-1,0,0]
count = 0

while queue:
    print(f'queue: {queue}')

    x,y,A = queue.popleft()
    print(f'(x, y) and A: {x}, {y}, {A}')
    
    for i in range(r):
        print(mirr[i])

    fire = 0
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        print(f'[nx][ny]: {nx}, {ny}, {mirr[nx][ny]}')
        #길이 있으면 - 이동하거나 불타거나
        if mirr[nx][ny] == '.':
            print('길이 있다! f인가 j인가? ')
            if A == 'F':
                mirr[nx][ny] = 'F'
                print(f'fire! {mirr[nx][ny]}')
                queue.append( (nx, ny, 'F') )
            elif A == 'J':
                print('move!')
                mirr[nx][ny] = mirr[x][y] + 1
                count = max(count, mirr[nx][ny]) #최댓값 계산
               
                queue.append( (nx, ny, 'J') )

        #가장자리 도달 - 탈출
        elif nx==r or nx == -1 or ny == c or ny == -1:
            print(max)
            break

        elif mirr[nx][ny]=='#' or mirr[nx][ny]=='F':
            fire += 1

        #탈출못하는경우
        elif fire == 4:
            print('IMPOSSIBLE')
            break