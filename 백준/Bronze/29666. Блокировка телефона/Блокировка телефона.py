cal = [[1,2,3],[4,5,6],[7,8,9]]
row = [[1,4,7],[2,5,8],[5,8,0],[3,6,9]]

a = set(map(int,input()))
if len(a) != 3:
    print('Locked')
    exit()

for p in (cal,row):
    for i in p:
        for j in a:
            if not j in i:
                break

        else:
            print('Unlocked')
            exit()

print('Locked')
