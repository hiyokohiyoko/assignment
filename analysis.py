import pegpy
peg = pegpy.grammar('sen.en.tpeg')
parser = pegpy.generate(peg)

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

from dictionary import dic1, dic2, dic3

#ベクトルの演算を定義する
import math

class space(object):
    pass

class Vec(space):
    def __init__(self, str: str): # 文字列を引数に取る　Vec("1 2 3")
        self.a = str.split(' ')   # 空白で分割した文字列のリストを保持する

    def __repr__(self):           # print()文で [1 2 3]と表示
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

    def dist(self, v):    # ベクトルが表す2点間の距離の計算
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
def v(arr): # 複数の抽出単語からなるリストを引数に取る
    s = 0   # 対象
    i = 50  # 興味 呟く時点で興味はあるのでデフォルトで50
    l = 0   # 好感度
    le = len(arr)
    for j in range(le):
        if arr[j] in dic1:  # 対象
            s = dic1[arr[j]]
        if arr[j] in dic2:  # 興味
            i = dic2[arr[j]]
        if arr[j] in dic3:  # 好感度
            l = dic3[arr[j]]
        if arr[j] not in dic1 and arr[j] not in dic2 and arr[j] not in dic3:
            n = int(input('set about ' + f'{arr[j]}.' + ' 1:subject, 2:interest, 3:likability : '))
            p = int(input('set integral parameter. -100~100 : '))
            if n == 1:
                s = p
                dic1[arr[j]] = p
            if n == 2:
                i = p
                dic2[arr[j]] = p
            if n == 3:
                l = p
                dic3[arr[j]] = p
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
    sub.append(s)  # グローバルリストに座標を追加
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

    #plot(Vec("0 1 2"))
    #plot(Vec("-50 40 70"))
    #vv = v(['python3', 'am_interested_in', 'like'])
    #plot(vv)
    #u = v(['viola', 'am_interested_in', 'love'])
    #plot(u)

    try:
        while True:
            s = input('input sentences or \'dist\' to know distance of two past sentences >>> ')
            if s == 'dist':   # 過去に呟いた文章同士の「距離」を計る
                ss = input('input two numbers(1 orogin) : ')
                num = ss.split(' ')
                a = int(num[0]) - 1
                b = int(num[1]) - 1
                v1 = Vec(str(sub[a]) + ' ' + str(inte[a]) + ' ' + str(like[a]))
                v2 = Vec(str(sub[b]) + ' ' + str(inte[b]) + ' ' + str(like[b]))
                print(v1.dist(v2))
                continue
            if s == 'correct':
                ss = input('word to correct parameter : ')
                print('current parameter : ', end = "")
                if ss in dic1:
                    print(dic1[ss])
                if ss in dic2:
                    print(dic2[ss])
                if ss in dic3:
                    print(dic3[ss])
                p = int(input('new parameter : '))
                print(f'{ss}' + ' : ' + str(p))
                if ss in dic1:
                    dic1[ss] = p
                if ss in dic2:
                    dic2[ss] = p
                if ss in dic3:
                    dic3[ss] = p
                continue
            if s == '':
                break
            t(s)
    except EOFError:
        return

if __name__ == '__main__':
    main()