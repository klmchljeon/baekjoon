#아침 태권도
import sys
from math import gcd
input = sys.stdin.readline

n = int(input())
st = set()

for _ in range(n):
    x,y = map(int,input().split())
    g = gcd(x,y)
    x//=g; y//=g
    st.add((x,y))

print(len(st))