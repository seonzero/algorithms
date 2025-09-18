s = input()
alpabets = [0] * 26
#단어에 포함된 a, b, ... z의 개수를 공백으로 구분해서 출력한다

for x in s:
    #알파벳 -> 숫자 변환 함수
    idx = ord(x) - 97
    alpabets[idx] += 1

for x in alpabets:
    print(x, end=" ")