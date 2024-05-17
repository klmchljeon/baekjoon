t = int(input())
for case in range(t):
    a,b = input().split()
    res = sorted(a) == sorted(b)
    p = 'NOT ' if not res else ''
    print(f'{a} & {b} are {p}anagrams.')