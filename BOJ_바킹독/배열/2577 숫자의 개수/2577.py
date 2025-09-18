# a,b,c -> a*b*c를 계산한 결과에 0~9 각각의 숫자가 몇번씩 쓰엿나 
# 예: 17037300 - 0이3번, 1이1번, 3이2번, 7이2번

a = int(input())
b = int(input())
c = int(input())

total = a*b*c

#아까 알파벳개수랑 비슷하게 접근하는데 대신 total을 int가 아니라 str로 변환해서 보면 될듯
s_total = str(total)

print(s_total)

nums = [0] * 10

for x in s_total:
    idx = int(x)
    nums[idx] += 1

for x in nums:
    print(x)