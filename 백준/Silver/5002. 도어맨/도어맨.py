def check(idx):
    return abs(res[idx]+1 - res[idx^1]) <= x

x = int(input())
st = input()

lst = [int(i=='M') for i in st[::-1]]
res = [0,0]
keep = None
while lst:
    if keep != None and check(keep):
        res[keep] += 1
        keep = None
        continue
    
    i = lst.pop()
    if check(i):
        res[i] += 1
        continue

    elif keep == None:
        keep = i
        continue

    break

print(sum(res))