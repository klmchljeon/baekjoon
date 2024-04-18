st = input()
for i in range(len(st)):
    tmp = st + st[:i][::-1]
    if tmp == tmp[::-1]:
        print(len(tmp))
        break