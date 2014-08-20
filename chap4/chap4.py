# /usr/bin/env python
# -*- coding:utf-8 -*-

## インデントとブロック構造
n = 9
r = 1
while n > 0:
    r = r * n                   # r *= nでもよい
    n = n - 1                   # n -= 1でもよい


## コメントの記述
# xに5を代入
x = 5
x = 3                           # x は 3 になる
x = "#これはコメントではない"

## 変数と代入
x = 5
x = "Hello"
print(x)

x = 5
print(x)

del x
# print(x) # エラー

## 式
x = 3
y = 5
z = (x + y) / 2
print(z)

## 文字列
x = "Hello, World"
x = "\t この文字列は\"タブ\"で始まります"
print(x)
x = "この文字列はバックスラッシュ(\\)を 1 つ含んでいます"
print(x)

x = "Hello, World"
x = 'Hello, World'

x = "'をバッククオートする必要はない"
x = 'バックスラッシュでエスケープしないと\'を表示できない'
x = "\"文字はバックスラッシュでエスケープ"
x = 'そのまま"を記述できる'

x =""" トリプルクオートの場合は改行や
「"」や「'」をバックスラッシュ無しで含むことができる"""


## 数値
print(5 + 2 - 3 * 2)
print(5 / 2)                    # 浮動小数点となる
print(5 / 2.0)                  # 同上
print(5 // 2)                   # 丸められて整数になる
print(3000000000)
print(30000000 * 3)
print(30000000 * 3.0)
print(2.0e-8)
print(int(200.2))               # intにまるめられる
print(int(200.9))
print(int(2e2))
print(float(200))               # floatに

## 組み込み数値演算
## 高度な数値関数
import math
help(math)

## 複素数
print(3+2j)
print(3 + 2j - (4 + 4j))
print((1+2j)*(3+4j))
print(1j*1j)

z = (3+5j)

print(z.real)                   # 複素数の実部と虚部はreal,imagでアクセス可能
print(z.imag)                   # 浮動小数点で返ってくる

## 高度な複素数関数
import cmath
help(cmath)
print(cmath.sqrt(-1))

## ユーザー入力を受け取る
name = input("Name? ")
print(name)

age = int(input("Age? "))
print(age)


