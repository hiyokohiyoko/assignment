
#ベクトルの演算を定義する
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
                va += str(int(self.a[i])+ int(v.a[i]))
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
                va += str(int(self.a[i]) - int(v.a[i]))
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
                sq += (int(self.a[i]) - int(v.a[i])) ** 2
            return math.sqrt(sq)
    
# 以下、動作確認
v1 = Vec("1 2 3")
print(v1)

v2 = Vec('4 5 6')
print(v2)
print(v1 + v2)
print(v1 - v2)
print(v1.dist(v2))

v3 = Vec('1 2 3 4')
print(v1 + v3)
print(v1 - v3)
print(v1.dist(v3))

