x,a,y,b,z = input().split()

xy = eval(x+a+y)
res = eval(str(xy)+b+z)

p = len('SASA CALCULATOR')
st1 = '''=================
|SASA CALCULATOR|'''

st2 = '''-----------------
|               |
| AC         /  |
| 7  8  9    *  |
| 4  5  6    -  |
| 1  2  3    +  |
|    0  .    =  |
================='''

print(st1)
print(f'|{res:{p}.3f}|')
print(st2)