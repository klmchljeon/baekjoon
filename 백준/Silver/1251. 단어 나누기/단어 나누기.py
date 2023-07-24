#단어 나누기
st = input()
n = len(st)

lst = []
for i in range(1,n-1):
    for j in range(i+1,n):
        tmp = st[:i][::-1] + st[i:j][::-1] + st[j:][::-1]
        lst.append(tmp)

lst.sort()
print(lst[0])