import math
n=int(input())
if n==1:
    print(1)
else:
    k = math.floor(math.log2(n-1))
    start = 2**k + 1
    print(2*(n-start+1))