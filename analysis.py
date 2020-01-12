import pegpy
peg = pegpy.grammar('sen.en.tpeg')
parser = pegpy.generate(peg)

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

#ベクトルの演算を定義する
import math

class Vec(object):
    def __init__(self, str: str):
        self.a = str.split(' ')

    def __repr__(self):
        str = '['
        for i in range(len(self.a)):
            str += self.a[i] 
            if i < len(self.a)-1:
                str += ' '
        str += ']'
        return str

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

#単語のベクトル化
def v(arr):
    s = 0
    i = 50  # 呟く時点で興味はある
    l = 0
    le = len(arr)
    for j in range(le):
        if arr[j] in dic1:  # 対象
            s = dic1[arr[j]]
        elif arr[j] in dic2:  # 興味
            i = dic2[arr[j]]
        elif arr[j] in dic3:  # 好感度
            l = dic3[arr[j]]
        else:
            n = input('set your word. 1:subject, 2:interest, 3:likability : ')
            p = input('set integral parameter. -100~100 : ')
            if n == 1:
                dic1[arr[j]] = p
                s = p
            elif n == 2:
                dic2[arr[j]] = p
                i = p
            else:
                dic3[arr[j]] = p
                l = p
        return Vec(str(s) + ' ' + str(i) + ' ' + str(l))

#構文木の解析
def ana(tree):
    if tree == 'Block':
        return ana(tree[0])
    if tree == 'Subj1':
        return ana(tree[0])
    if tree == 'Subj2':
        return ana(tree[0])
    if tree == 'Subj3':
        return ana(tree[0])
    if tree == 'NSubj':
        return ana(tree[0])
    if tree == 'Sent1':
        return v([tree[0], tree[1], tree[2]])
    if tree == 'Sent2':
        return v([tree[0], tree[1], tree[2]])
    if tree == 'Sent3':
        return v([tree[0], tree[1], tree[2]])
    if tree == 'Sent4':
        return v([tree[0], tree[1]])
    if tree == 'Sent5':
        return v([tree[0], tree[1]])
    if tree == 'Sent6':
        return v([tree[0], tree[1]])
    if tree == 'Sent7':
        return v([tree[0], tree[1]])
    if tree == 'Sent8':
        return v([tree[0], tree[1]])
    if tree == 'Sent9':
        return v([tree[0]])

#ベクトルのグラフへのプロット
def plot(vec: Vec):
    print(vec)

    s = int(vec.a[0])
    i = int(vec.a[1])
    l = int(vec.a[2])
    sub.append(s)
    inte.append(i)
    like.append(l)

    ss = np.array(sub)
    ii = np.array(inte)
    ll = np.array(like)

    fig = plt.figure()
    ax = fig.add_subplot(projection='3d')
    # ax.legend()
    ax.set_title('result of analysis', fontsize = 15)
    ax.set_xlim(-100, 100)
    ax.set_ylim(-100, 100)
    ax.set_zlim(-100, 100)
    ax.set_xlabel('subject')
    ax.set_ylabel('interest')
    ax.set_zlabel('likability')
    ax.scatter(ss, ii, ll, s = 50, c = 'c', marker = 'o', alpha = 1)
    fig.show()

#構文解析
def t(s: str):
    tree = parser(s)
    if tree.isError():
        print('Error')
    else:
        vec = ana(tree)
        plot(vec)

sub = []      #グローバル変数
inte = []
like = []

def main():
    # 最初にグラフを出しておく
    fig = plt.figure()
    ax = fig.add_subplot(projection='3d')
    # ax.legend()
    ax.set_title('result of analysis', fontsize = 15)
    ax.set_xlim(-100, 100)
    ax.set_ylim(-100, 100)
    ax.set_zlim(-100, 100)
    ax.set_xlabel('subject')
    ax.set_ylabel('interest')
    ax.set_zlabel('likability')
    fig.show()

    plot(Vec("0 1 2"))
    plot(Vec("-50 40 70"))

    try:
        while True:
            s = input('input sentences or \'dist\' to know distance of two past sentences >>> ')
            if s == 'dist':
                ss = input('input two numbers(1 orogin) : ')
                num = ss.split(' ')
                a = int(num[0]) - 1
                b = int(num[1]) - 1
                v1 = Vec(str(sub[a]) + ' ' + str(inte[a]) + ' ' + str(like[a]))
                v2 = Vec(str(sub[b]) + ' ' + str(inte[b]) + ' ' + str(like[b]))
                print(v1.dist(v2))
                continue
            if s == '':
                break
            t(s)
    except EOFError:
        return

if __name__ == '__main__':
    main()