lst = [[0,1,2,3],[0,1,4,5],[0,2,4,6],[1,3,5,7],[2,3,6,7],[4,5,6,7]]
t = int(input())
for case in range(t):
    tmp = sorted(map(int,input().split()))
    print('YES' if tmp in lst else 'NO')