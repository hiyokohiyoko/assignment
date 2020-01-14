
#ベクトルと行列の演算を定義する
import math

class Vec(object):
    def __init__(self, s: str):
        self.a = s.split(' ')
    
    def __repr__(self):
        s = '['
        for i in range(len(self.a)):
            s += self.a[i] 
            if i < len(self.a)-1:
                s += ' '
        s += ']'
        return s
    
    def __add__(self, v):
        if len(self.a) != len(v.a):
            print('these vectors are not for adding.')
            return
        else:
            va = ''
            for i in range(len(self.a)):
                va += str(float(self.a[i])+ float(v.a[i]))
                if i < len(self.a) - 1:
                    va += ' '
            return Vec(va)
    
    def __sub__(self, v):
        if len(self.a) != len(v.a):
            print('these vectors are not for subtraction.')
            return
        else:
            va = ''
            for i in range(len(self.a)):
                va += str(float(self.a[i]) - float(v.a[i]))
                if i < len(self.a) - 1:
                    va += ' '
            return Vec(va)
    
    def dist(self, v):
        if len(self.a) != len(v.a):
            print('these vectors are not in the same space.')
            return
        else:
            sq = 0
            for i in range(len(self.a)):
                sq += (float(self.a[i]) - float(v.a[i])) ** 2
            return math.sqrt(sq)
    
    def inpro(self, v):
        if len(self.a) != len(v.a):
            print('these vectors are not in the same space.')
            return
        else:
            inn = 0
            for i in range(len(self.a)):
                inn += (float(self.a[i]) * float(v.a[i]))
            return inn

class Mat(object):
    def __init__(self, ar):  # arは文字列(行ベクトル)のリスト
        l = len(ar)
        self.a = []
        for i in range(l):
            self.a.append(ar[i].split(' '))
    
    def __repr__(self):
        n = len(self.a)  # n行
        m = len(self.a[0])  # m列
        for i in range(n):
            for j in range(m):
                if i + j == 0:
                    print('[', end = '')
                print(self.a[i][j], end = '')
                if j < m - 1:
                    print(' ', end = '')
                if j == m - 1 and i < n - 1:
                    print()
                if j == m - 1 and i == n - 1:
                    print(']')
        return ''

    def __add__(self, mat):
        n = len(self.a)
        m = len(self.a[0])
        k = len(mat.a)
        l = len(mat.a[0])
        if n != k or m != l:
            print('they are not for adding.')
            return
        ans = []
        s = ''
        for i in range(n):
            s = ''
            for j in range(m):
                s += str(float(self.a[i][j]) + float(mat.a[i][j])
                if j < m-1:
                    s += ' '
            ans.append(s)
        return ans

    def __sub__(self, mat):
        n = len(self.a)
        m = len(self.a[0])
        k = len(mat.a)
        l = len(mat.a[0])
        if n != k or m != l:
            print('they are not for subtraction.')
            return
        ans = []
        s = ''
        for i in range(n):
            s = ''
            for j in range(m):
                s += str(float(self.a[i][j]) - float(mat.a[i][j])
                if j < m-1:
                    s += ' '
            ans.append(s)
        return ans

    def __mul__(self, mat):
        n = len(self.a)
        m = len(self.a[0])
        k = len(mat.a)
        l = len(mat.a[0])
        if m != k:
            print('they are not for multiplication.')
            return
        ans = []
        s = ''
        for i in range(n):
            s = ''
            for j in range(l):
                sum = 0
                for h in range(m):
                    sum += float(self.a[i][h]) * float(mat.a[h][j])
                s += str(sum)
                if j < l-1:
                    s += ' '
            ans.append(s)
        return ans
    

# 以下、動作確認
v1 = Vec("1 2 3")
print(v1)

v2 = Vec('4 5 6')
print(v2)
print(v1 + v2)
print(v1 - v2)
print(v1.dist(v2))
print(v1.inpro(v2))

v3 = Vec('1 2 3 4')
print(v1 + v3)
print(v1 - v3)
print(v1.dist(v3))
print(v1.inpro(v3))

m1 = Mat(['1 2 3', '4 5 6', '7 8 9'])
print(m1)

m2 = Mat(['2 3 4', '5 6 7', '8 9 10'])
print(m2)
print(m1 + m2)
print(m1 - m2)
print(m1 * m2)

m3 = Mat(['1 2 3', '4 5 6', '7 8 9', '10 11 12'])
print(m1 * m3)