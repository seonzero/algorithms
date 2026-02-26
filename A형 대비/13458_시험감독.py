N = int(input())
lst = list(map(int, input().split()))
B, C = map(int, input().split())
result = 0

for i in lst:
    #학생수 - 총감독관수
    num = i - B
    count = 1
    
    #남은 학생이 있다면... 
    if num>0:
        # 부감독수보다 작으면 cnt+1
        if num < C:
            count += 1
        #부감독수보다 많다면
        else:
            #배수라면
            if num%C==0:
                count += num/C
            else: 
                count += num//C 
                count += 1

    result += count 

print(int(result))

