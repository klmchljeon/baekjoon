class Matrix:
    def __init__(self,n,m,lst):
        self.row = n
        self.col = m
        self.lst = lst

    def __add__(self,other):
        if self.row != other.row or self.col != other.col:
            return None
        
        res = []
        for i in range(self.row):
            tmp = []
            for j in range(self.col):
                s = self.lst[i][j] + other.lst[i][j]
                tmp.append(s)

            res.append(tmp)

        return Matrix(self.row, self.col, res)
    
    def __mul__(self,other):
        if self.col != other.row:
            return None
        
        res = []
        for i in range(self.row):
            tmp = []
            for j in range(other.col):
                s = 0
                for k in range(self.col):
                    s += self.lst[i][k]*other.lst[k][j]

                tmp.append(s)

            res.append(tmp)

        return Matrix(self.row, other.col, res)
    
    def __str__(self):
        res = []
        for i in self.lst:
            res.append(' '.join(map(str,i)))

        return '\n'.join(res)
    
tmp = []
for _ in range(2):
    n,m = map(int,input().split())
    lst = [list(map(int,input().split())) for _ in range(n)]
    tmp.append(Matrix(n,m,lst))

a,b = tmp
print(a*b)