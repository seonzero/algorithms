import sys
input = sys.stdin.readline

n = int(input())
#오름차순정렬이 필요하다 - sorted
arr = sorted(list(map(int, input().split())))
x = int(input())

result = 0
left, right = 0, arr_len -1

while left<right:
    temp = arr[left] + arr[right]

    #기본적으로 left인덱스를 +1해주면서 합이 x인지 체크를 하되
    if temp == x :
        res +=1
        left += 1
    elif temp < x:
        left += 1

    #두 합이 x보다 클 때만 right인덱스를 -1해준다 
    else:
        right +=1 

print(result)

'''
참고링크: 
https://ghi512.tistory.com/121
https://gyujh.tistory.com/62
'''