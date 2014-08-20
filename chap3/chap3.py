# /usr/bin/env python3
# -*- coding:utf-8 -*-

x = 5 + 2 - 3 * 2

print(x)

# 割り算
print(5 / 2)

# 切り捨て
print(5 // 2)

# 余り
print(5 % 2)


print(2 ** 8)

print(1000000001 ** 3)

print(4.3 ** 2.4)

print(3.5e30 * 2.77e45)

print(10000000001.0 ** 3)

print((3+2j) ** (2+3j))

x= (3 + 2j) * (4 + 9j)

print(x)

print(x.real, x.imag)

print(round(3.49))

import math
print(math.ceil(3.49))

# Bool
x = False
print(x)

print(not x)

# Trueは1,Falseは0のように振る舞う
y = True * 2

print(y)

# リスト
print([])
print([1])
print([1,2,3,4,5,6,8,12])
print([1, "two", 3, 4.0, ["a", "b"], (5,6)])

# インデックス指定
x = ["first", "second", "third", "fourth"]

print(x[0])
print(x[2])
print(x[-1])
print(x[-2])
print(x[1:-1])
print(x[0:3])
print(x[-2:-1])
print(x[:3])
print(x[-2:])

x = [1, 2, 3, 4, 5, 6, 7, 8, 9]

x[1] = "two"
print(x)

x[8:9] = []
print(x)

x[5:7] = [6.0, 6.5, 7.0]
print(x)

print(x[5:])

# リストのメソッド
x = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(len(x))

# xはそのまま
print([-1, 0] + x)

x.reverse()
print(x)

# タプル
print(())
print((1,))                     # 要素が一つしかない場合カンマが必要
print((1,2,3,4,5,6,12))
print((1,"two", 3, 4.0, ["a", "b"], (5, 6)))

x = [1,2,3,4]
print(tuple(x))                 # リストからタプルへ

x = (1,2,3,4)
print(list(x))                 # タプルからリストへ


## 文字列
x = "live and  let \t \tlive"
print(x.split())                # 空白文字でsplitする

print(x.replace(" let \t \tlive", "enjoy life"))

import re                       # 正規表現
regexpr = re.compile(r"[\t ]+")
print(regexpr.sub(" ", x))

# print関数の使い方
e = 2.718
x = [1, "two", 3, 4.0, ["a", "b"], (5,6)]
print("The constant e is:", e, "and the list x is:", x)
print("the value of %s is %.2f" % ("e", e))


## 辞書
#キーは変更不能な型でないといけない
x = {1:"one", 2:"two"}
x["first"]="one"
x[("Delorme", "Ryan", 1995)] = (1,2,3)

print(list(x.keys()))
print(x[1])

# 要素が存在しない場合、getはオプションでユーザー定義の値を返す
print(x.get(1, "not available"))
print(x.get(4, "not available"))

print(x.get(4))                 # 要素が存在しない場合、例外でなくNoneを返す

## 集合
x = set([1,2,3,1,3,5])
print(x)

print(1 in x)
print(4 in x)

f = open("myfile", "w")
print(f.write("First line with necessary newline character\n"))
print(f.write("Second line to write to the file \n"))
f.close()

f = open("myfile", "r")
line1 = f.readline()
line2 = f.readline()
f.close()

print(line1, line2)

import os
print(os.getcwd())
os.chdir(os.path.join("/home", "ym", "Documents"))

filename = os.path.join("/home", "ym", "project", "quick-python", "chap3", "myfile")
print(filename)

f = open(filename, "r")
print(f.readline())

f.close()

## 制御フロー
x = 5
if x < 5:
    y = -1
    z = 5
elif x > 5:
    y = 1
    z = 11
else:
    y = 0
    z = 10

print(x, y, z)


# whileループ
u, v, x, y = 0, 0, 100, 30
while x > y:
    u = u + y
    x = x - y
    if x < y + 2:
        v = v + x
        x = 0
    else:
        v = v + y + 2
        x = x - y - 2
print(u, v)

# forループ
item_list = [3, "sring1", 23, 14.0, "string2", 49, 64, 70]

for x in item_list:
    if not isinstance(x, int):
        continue
    if not x % 7:
        print("found an integer divisivle by seven %d" % x)
        break

## 関数定義
def funct1(x, y , z):
    value = x + 2*y + z ** 2
    if value > 0:
        return x + 2 * y +z**2
    else:
        return 0

u, v = 3, 4
print(funct1(u, v, 2))

print(funct1(u, z=v, y=2))

def funct2(x, y=1, z=1):
    return x + x*y + z**2
    
print(funct2(3, z=4))

def funct3(x, y=1, z=1, *tup):
    print((x,y,z) + tup)

funct3(2)
funct3(1,2,3,4,5,6,7,8,9)

def funct4(x, y=1, z=1, **dict):
    print(x, y, z, dict)

funct4(1, 2, m=5, n=9, z=3)

## 例外
class EmptyFileError(Exception):
    pass


filenames = ["myfile1", "nonExistent", "emptyFile", "myfile2"]
for file in filenames:
    try:
        f = open(file, 'r')
        line = f.readline()     # IOErrorが発生する可能性がある
        if line == "":
            f.close()
            raise EmptyFileError("%s: is empty" % file)
    except IOError as error:
        print("%s : could not be opened: %s" %(file, error.strerror))
    except EmptyFileError as error:
        print(error)
    else:
        print("%s: %s" % (file, f.readline()))
    finally:                    # 例外が発生したかどうかに関わらず常に実行される
        print("Done processing", file)


## モジュール
import sys
print(sys.path)

os.chdir(os.path.join("/home", "ym", "project", "quick-python", "chap3"))

import wo
wo.words_occur()

# モジュールのリロード
import imp
imp.reload(wo)

## オブジェクト指向プログラミング 
import sh
c1 = sh.Circle()
c2 = sh.Circle()
print(c1)
print(c2)
print(c2.area())

c2.move(5, 6)
print(c2)

