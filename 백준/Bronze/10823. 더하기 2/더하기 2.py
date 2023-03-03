#더하기 2
import sys
input = sys.stdin.read

st = input().replace('\n','')
res = sum(map(int,st.split(',')))
print(res)