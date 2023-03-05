#도비의 난독증 테스트
import sys
input = sys.stdin.read

st = input().split()

res = []
tmp = []
for i in st[1:]:
    if i.isdigit():
        tmp.sort()
        res.append(sorted(tmp)[0][1])
        tmp = []

    else:
        tmp.append((i.lower(),i))

print(*res,sep='\n')