t = int(input())

for _ in range(t):
  pw = input()
  pw1 = []
  pw2 = []

  for i in pw:
    if i=='<':
       if pw1:
        pw2.append(pw1.pop())
    elif i=='>':
        if pw:
            pw1.append(pw2.pop())
    elif i=='-':
        pw1.pop()
    else:
       pw1.append(i)

    print(pw1, pw2)