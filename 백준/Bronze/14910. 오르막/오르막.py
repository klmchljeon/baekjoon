d = list(map(int,input().split()))
res = sorted(d) == d
print('Good' if res else 'Bad')