a,b,c = map(int,input().split())
res = (a-11)*24*60 + (b-11)*60 + (c-11)
print(res if res >= 0 else -1)