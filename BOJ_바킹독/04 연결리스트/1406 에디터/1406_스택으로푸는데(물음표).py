# 한줄로 된 에디터
# 영어 소문자만을 기록할 수 있다

# 참고 https://mxxcode.tistory.com/39

import sys
input = sys.stdin.readline

st1 = list(input().strip())
st2 = []
n = int(input())

for i in range(n):
    c = input().split()
    if c[0] == 'L' and st1:
        st2.append(st1.pop())
    elif c[0] == 'D' and st2:
        st1.append(st2.pop())
    elif c[0] == 'B' and st1:
        st1.pop()
    elif c[0]=='P':
        st1.append(c[1])

st1.extend(reversed(st2))
print(''.join(st1))