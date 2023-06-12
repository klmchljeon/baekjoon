#후위 표기식2 
conv = lambda x:ord(x)-ord('A')

n = int(input())
st = input()

cnt = 0
for i in st:
    if 'A' <= i <= 'Z':
        cnt = max(cnt,conv(i)+1)

d = [int(input()) for _ in range(cnt)]

stack = []
for i in st:
    if 'A' <= i <= 'Z':
        stack.append(d[conv(i)])

    else:
        b = stack.pop()
        a = stack.pop()
        stack.append(float(eval(str(a)+i+str(b))))

print(f'{stack[0]:0.2f}')