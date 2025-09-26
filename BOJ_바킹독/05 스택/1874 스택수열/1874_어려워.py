# 스택을 활용하기
# 1부터 n까지의 수를 스택에 넣었다가 뽑아서 늘어놓기 -> 하나의 수열 만들기
# 이때 스택에 push하는 순서 - 오름차순
# 임의의 수열이 주어졌을 때 스택을 이용해서 그 수열을 만들수 있는지 / 어떤 순서로 push, pop연산을 수행해야 하는지

n = int(input())

'''
sample = []
for _ in range(n):
    sample.append(int(input()))
'''

sample = list(int(input()) for _ in range(n))
print(f'sample: {sample}')

stck = []
idx=0
make = []
make_arr = []
i = 1

#이제 샘플이랑 비교하면서 스택에 넣엇다뺏다 할거임
#오름차순 준비완료: for i in range(1, n+1) (1부터 n까지)
#for i in range(2, n+1):
while True:
    if len(stck)==n:
        break
    if len(stck) >=2 and sample[idx] == stck[-1]:
        make.append(stck.pop())
        make_arr.append('-')
        idx +=1
    else:
        stck.append(i)
        make_arr.append('+')
        i += 1
    print(f'make: {make}, stck: {stck}')

if sample == make:
    print(make_arr)
else: 
    print('NO')