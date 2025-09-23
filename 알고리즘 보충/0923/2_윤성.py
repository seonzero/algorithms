N = int(input())
cnt = 0


def KFC(length):
    global cnt
    if length == N: 
        cnt += 1
    for i in range(1, 5):
        if length + i > N: 
            break
        KFC(length + i)


KFC(0)
print(cnt)
