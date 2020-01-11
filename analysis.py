import pegpy
peg = pegpy.grammar('sen.en.tpeg')
parser = pegpy.generate(peg)

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

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

    def inpro(self, v):  # 内積
        if len(self.a) != len(v.a):
            print('these vectors are not in the same space.')
            return
        else:
            inn = 0
            for i in range(len(self.a)):
                inn += (float(self.a[i]) * float(v.a[i]))
            return inn

def ana(tree):
    pass

def plot(vec: Vec):
    

def t(s: str):
    tree = parser(s)
    if tree.isError():
        print('Error')
    else:
        vec = ana(tree)
        plot(vec)

def main():
    fig = plt.figure()
    ax = fig.add_subplot(projection='3d')
    ax.legend()
    plt.title('result of analysis')
    ax.set_xlim(-100, 100)
    ax.set_ylim(-100, 100)
    ax.set_zlim(-100, 100)
    ax.set_xlabel('subject')
    ax.set_ylabel('interest')
    ax.set_zlabel('likability')
    fig.show()
    try:
        while True:
            s = input('>>> ')
            if s == '':
                break
            t(s)
    except EOFError:
        return

if __name__ == '__main__':
    main()