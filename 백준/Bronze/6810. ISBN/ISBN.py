lst = list(map(int,'9780921418'))
for i in range(3):
    lst.append(int(input()))

res = 0
for i in range(len(lst)):
    res += lst[i]*(1 if i%2==0 else 3)

print(f'The 1-3-sum is {res}')