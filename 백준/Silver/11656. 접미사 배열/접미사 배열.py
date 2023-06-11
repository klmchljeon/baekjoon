#접미사 배열
st = input()
lst = []

tmp = ''
for i in range(len(st)-1,-1,-1):
    tmp = st[i] + tmp
    lst.append(tmp)

lst.sort()
print(*lst,sep='\n')