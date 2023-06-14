#시리얼 번호
n = int(input())
d = []
for _ in range(n):
    s = input()
    num = 0
    for i in s:
        if '0' <= i <= '9':
            num += int(i)

    tmp = [len(s),num,s]
    d.append(tmp)

d.sort()
for i in d:
    print(i[-1])