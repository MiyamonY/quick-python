# /usr/bin/env python
# -*- coding:utf-8 -*-

## リストは配列に似ている
# 3つの要素からなるリストをxに代入
x = [1, 2, 3]

x = [2, "tow", [1, 2, 3]]
print(len(x))                   # リストの要素数を返す

## リストのインデックス
x = ["first", "second", "third", "fourth"]

print(x[0])                     # インデックスは0から
print(x[2])

a = x[-1]
print(a)                        # -1といった指定もできる
print(x[-2])

print(x[1:-1])
print(x[0:3])
print(x[-2:-1])

print(x[-1:2])                  # インデックスが逆転している場合nilとなる

print(x[:3])                    # リストの先頭から
print(x[2:])                    # リストの最後まで

y = x[:]                        # リストのコピー
y[0] = '1 st'

print(x, y)

## リストの変更
x = [1, 2, 3, 4]
x[1] = "two"                    # リストの要素の変更

print(x)

x = [1, 2, 3, 4]
x[len(x):] = [5,6,7]            # リストの末尾に追加
print(x)

x[:0] = [-1, 0]                 # リストの先頭に追加
print(x)

x[1:-1] = []                    # リストの要素を削除
print(x)

x = [1, 2, 3]
x.append("four")                # リストの末尾に要素を追加
print(x)

x = [1, 2, 3, 4]
y = [5, 6, 7]

x.append(y)
print(x)                        # リストの要素として追加されてしまう

x = [1, 2, 3, 4]
y = [5, 6, 7]
x.extend(y)                     # リストの結合はextendを使えばいい
print(x)

x = [1, 2, 3]
x.insert(2, "hello")            # 任意の場所に要素を追加
print(x)

x.insert(0, "start")
print(x)

x = [1, 2, 3]
x.insert(-1, "hello")           # insertのインデックスは負の値も使用できる

print(x)

x = ['a', 2, 'c', 7, 9, 11]
del x[1]                        # 要素を削除
print(x)

del x[:2]                       # スライスも使用できる
print(x)

x = [1, 2, 3, 4, 3, 5]
x.remove(3)                     # removeはインデックスではなく、要素を指定する
print(x)
x.remove(3)
print(x)
# x.remove(3) 要素がない場合は例外を出す

x = [1, 3, 5, 6, 7]
x.reverse()                     # 要素をひっくり返す
print(x)

## リストのソート
x = [3, 8, 4, 0, 2, 1]
x.sort()
print(x)

x = [2, 4, 1, 3]
y = x.copy()                    # copy関数でコピーができる。x[:]でも同じ

y.sort()
print(x, y)

x = ["Life", "is", "Enchantng"]
x.sort()
print(x)

x = [1, 2, 'hello', 3]
# x.sort() エラー 数値と文字列は比較できないため

x = [[3, 5], [2, 9], [2, 3], [4, 1], [3, 2]]
x.sort()                        # 辞書式ソート
print(x)

## 独自の方法でソート
def compare_num_of_chars(string1):
    return len(string1)

word_list = ['Python', 'is', 'better', 'than', 'C']

word_list.sort()
print(word_list)

word_list.sort(key=compare_num_of_chars)
print(word_list)

# 降順でソートしたい場合は、sortのreverseパラメータをTrueにするか、
# sortした後、reverseする。

## sorted関数
x = (4, 3, 1, 2)
y = sorted(x)                   # sortedにもkey,reverseパラメータがある
print(y)

## その他の一般的なリスト操作
print(3 in [1, 3, 4, 5])        # in演算子でリストにその要素が含まれているかを判定できる
print(3 not in [1, 3, 4, 5])
print(3 in ["one", "two", "three"])
print(3 not in ["one", "two", "three"])

z = [1, 2, 3] + [4, 5]          # リストを連結する
print(z)

## *演算子にようるリストの初期化
z = [None] * 4                  # appendでリストを追加していくより、最初にリストを作る方が効率が良くなる
print(z)

z = [3, 1] * 2
print(z)

# minとmaxによるリストの最大値と最小値の検索
print(min([3, 7, 0, -2, 11]))
# print(max([4, "Hello", [1, 2]])) エラー 数値と文字列は比較できない

# indexによるリストの検索
x = [1, 3, "five", 7, -2]
print(x.index(7))               # 要素でリストを検索してインデックスを返す

# x.index(5) エラー 要素が存在しない場合は例外を出す

# countによるリストの検索
x = [1, 2, 2, 3, 5, 2, 5]
print(x.count(2))                # 含まれている要素の数を返す
print(x.count(5))
print(x.count(4))               # 存在しない場合は0を返す.例外は出ない

## ネストしたリストと深いコピー
m = [[0, 1, 2], [10, 11, 12], [20, 21, 22]]
print(m[0])
print(m[0][1])
print(m[2])
print(m[2][2])

# ネストされたリストの問題
nested = [0]
original = [nested, 1]
print(original)

nested[0] = 'zero'
print(original)                 # 参照により値が変わる

original[0][0] = 0
print(nested)                   # 参照により値が変わる
print(original)

nested = [2]                    # 別のオブジェクトを入れたら参照は消える
print(original)

# x[:]やx.copyはシャローコピー
original = [[0], 1]
shallow = original[:]
import copy
deep = copy.deepcopy(original)  # ディープコピーもできる

shallow[1] = 2
print(shallow)
print(original)

shallow[0][0] = 'zero'
print(original)                 # シャローコピーだと参照が残っており、こちらも値が変わる

deep[0][0] = 5
print(deep, original)

### タプル
## タプルの基礎
x = ('a', 'b', 'c')
print(x[2])
print(x[1:])
print(len(x))
print(max(x))
print(min(x))
print(5 in x)
print(5 not in x)

# タプルとリストは同じメソッドが使用でき殆ど同じだが、ミュータブルかイミュータブルの違いがある
# x[2] = 'd' エター イミュータブルだから値を変えることができない

print(x + x)                    # 新しいタプルを作る
print(2 * x)

# タプルのコピー
print(x[:])
print(x * 1)
print(x + ())

# タプルの要素にミュータブルな値は使用できるが、辞書のキーにはできない
x = ([1], [2], [3])
x[0][0] = 3
print(x)

# x[0] = [1,2] タプルの要素は変えれない

# 1要素のタプルはカンマが必要
x = 3
y = 4
print((x + y))
print((x+y,))                   # タプルにするにはコンマが必要

print(())                       # 空のタプルはコンマは必要ない

## タプルのパックとアンパック
(one, two, three, four) = (1, 2, 3, 4) # パターンマッチが可能
print(one, two)

one, two, three, four = 1, 2, 3, 4 # タプルは括弧の省略が可能

one = 1; two = 2; three = 3; four = 4 # と同じ

# スワップは以下のようにしなくても
var1 = 1; var2 = 2
temp = var1
var1 = var2
var2 = temp

# 次のように書ける
var1, var2 = var2, var1

x = (1, 2, 3, 4)
a, b, *c = x                    # *で残りの要素を取れる
print(a, b, c)

a, *b, c = x                    # 真ん中に書くこともできる
print(a, b, c)

*a, b, c = x                    # 最初でも
print(a, b, c)

a, b, c , d, *e = x
print(a, b, c, d, e)            # 対応する要素がない場合はnilになる

# アンパックはリストでも可能
[a, b] = [1, 2]
[c, d] = 3, 4
[e, f] = (5, 6)
(g, h) = 7, 8
i, j = [9 ,10]
k, l = (11, 12)

print(a)
print(a, [b, c, d], (e, f, g), h, i, j, k, l)

## リストとタプル間の変換
print(list((1, 2, 3, 4)))
print(tuple([1, 2, 3, 4]))

print(list("Hello"))            # listは文字列を文字にバラすことができる

### 集合
# 集合の要素はイミュータブルである必要がある

## 集合の操作
x = set([1, 2, 3, 1, 3, 5])
print(x)
x.add(6)
print(x)
x.remove(5)
print(x)
print(1 in x)
print(4 in x)

y = set([1, 7, 8, 9])
print(x | y)
print(x & y)
print(x ^ y)                    # 対象差(片方にしか含まれていないものを集める)

## frozenset
x = set([1, 2, 3, 1, 3 , 5])
z = frozenset(x)
print(z)
# z.add(6) frozensetはイミュータブル

# x.add([1]) エラー ミュータブルな要素は集合の要素にできない
x.add(z)                        # frozensetはイミュータブルなのでaddする事ができる
print(x)




























