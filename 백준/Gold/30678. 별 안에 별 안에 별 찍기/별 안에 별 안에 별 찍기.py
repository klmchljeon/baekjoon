#별 안에 별 안에 별 찍기
def star(num):
    if not num:
        return ['*']
    
    sub = star(num-1)
    l = 5**(num-1)
    d = []
    for i in sub:
        d.append(' '*l*2 + i + ' '*l*2)
    for i in sub:
        d.append(' '*l*2 + i + ' '*l*2)
    for i in sub:
        d.append(i*5)
    for i in sub:
        d.append(' '*l + i*3 + ' '*l)
    for i in sub:
        d.append(' '*l + i + ' '*l + i + ' '*l)

    return d

n = int(input())
print('\n'.join(star(n)))