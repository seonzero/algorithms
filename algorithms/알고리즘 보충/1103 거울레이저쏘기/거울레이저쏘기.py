n = int(input())
grid = [ list(input()) for _ in range(n)]   
k = int(input())

#좌표를 저장해둠. 
dx = [-1,0,1,0]
dy = [0,1,0,-1]
#이때 북0, 동1, 남2, 서3

def in_range(y, x):
    return 0<=y<n and 0<=x<n

def get_start_dir(k):
    if 1<=k<=n:
        return 2
    if n<k<=2*n:
        return 3
    if 2*n < k <= 3*n:
        return 0
    if 3*n < k <=4*n:
        return 1

def get_start_pos(k):
    if 1 <= k <= n:
        return 0, k - 1
    if n < k <= 2 * n:
        return (k - 1) - n, n - 1
    if 2 * n < k <= 3 * n:
        return n - 1, 3 * n - k
    if 3 * n < k <= 4 * n:
        return 4 * n - k, 0
    

y, x = get_start_pos(k) #k에 따라서 시작하는 좌표를 구하고
d = get_start_dir(k) #k에 따라서 시작하는 방향을 구함
cnt = 0

def reflect(y, x, d):
    mirror = grid[y][x]

    if mirror == '/':
        if d==0:
            return 1
        elif d==1:
            return 0
        elif d==2:
            return 3
        else:
            return 2
        
    if mirror=='\\':
        if d==0:
            return 3
        elif d==1:
            return 2
        elif d==2:
            return 1
        else:
            return 0
    

while in_range(y, x):
    #받은 좌표
    d = reflect(y, x, d)
    cnt +=1 
    #좌표이동
    y += dy[d]
    x += dx[d]

print(cnt)
