n = int(input())
lst = list(map(int,input().split()))
dic = dict()
for i in lst:
    if not i in dic:
        dic[i] = 0

    dic[i] += 1

print(max(dic.values()))